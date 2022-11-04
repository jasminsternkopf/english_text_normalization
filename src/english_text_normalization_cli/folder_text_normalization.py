from argparse import ArgumentParser, Namespace
from functools import partial
from logging import Logger
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Callable, Optional, Tuple, cast

from tqdm import tqdm

from english_text_normalization.auxiliary_methods.operations import (build_normalizer,
                                                                     get_valid_operations)
from english_text_normalization.auxiliary_methods.txt_files_reading import get_text_files
from english_text_normalization_cli.globals import ExecutionResult
from english_text_normalization_cli.helper import (get_optional, parse_codec,
                                                   parse_existing_directory,
                                                   parse_non_empty_or_whitespace, parse_path,
                                                   parse_positive_integer)


def get_folder_normalizing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command normalizes English text."
  parser.add_argument("directory", type=parse_existing_directory, metavar="DIRECTORY",
                      help="directory containing texts")
  parser.add_argument("operations", type=parse_non_empty_or_whitespace, metavar="OPERATION",
                      choices=get_valid_operations(), nargs="+", help="operations to apply; order will be considered; same operation can be applied multiple times")
  parser.add_argument("-o", "--output-directory", type=parse_path, metavar="OUTPUT",
                      help="custom directory to output normalized texts (existing texts will be overwritten); defaults to the input directory if it is not set", default=None)
  parser.add_argument("-e", "--encoding", type=parse_codec,
                      default="UTF-8", help="encoding of the texts")
  parser.add_argument("-j", "--n-jobs", metavar='N', type=parse_positive_integer,
                      choices=range(1, cpu_count() + 1), default=cpu_count(), help="amount of parallel cpu jobs")
  parser.add_argument("-c", "--chunksize", type=parse_positive_integer, metavar="NUMBER",
                      help="amount of files to chunk into one job", default=10)
  parser.add_argument("-mt", "--maxtasksperchild", type=get_optional(parse_positive_integer), metavar="NUMBER",
                      help="amount of tasks per child", default=None)
  return folder_normalize_ns


def folder_normalize_ns(ns: Namespace, logger: Logger, flogger: Logger) -> ExecutionResult:
  inp_dir = cast(Path, ns.directory)

  output_directory = cast(Path, ns.output_directory)
  if output_directory is None:
    output_directory = inp_dir

  paths = list(tqdm(get_text_files(inp_dir), desc="Collecting text files", unit="f"))
  logger.info(f"Collected {len(paths)} files.")
  normalizer = build_normalizer(ns.operations)

  pool_method = partial(
    process_path,
    encoding=ns.encoding,
    inp_dir=inp_dir,
    out_dir=output_directory,
  )

  with Pool(
    processes=ns.n_jobs,
    initializer=__init_pool_prepare_cache_mp,
    initargs=(normalizer,),
    maxtasksperchild=ns.maxtasksperchild,
  ) as pool:
    iterator = pool.imap(pool_method, paths, ns.chunksize)
    iterator = tqdm(iterator, total=len(paths), desc="Normalizing files", unit=" file(s)")
    result = list(iterator)

  success_count = 0
  for _, ex_info in result:
    if ex_info is None:
      success_count += 1
    else:
      msg, ex = ex_info
      flogger.error(msg)
      flogger.debug(ex)

  all_successful = success_count == len(paths)
  if not all_successful:
    logger.warning(
      f"Not everything was successful! Errors occurred on {len(paths)-success_count}/{len(paths)} file(s).")

  changed_count = sum(changed_anything for changed_anything, _ in result)
  changed_anything = changed_count > 0
  if changed_anything:
    logger.info(f"Changed content of {changed_count}/{len(paths)} files.")

  return all_successful, changed_anything


process_method: Callable[[str], str] = None


def __init_pool_prepare_cache_mp(method: Callable[[str], str]) -> None:
  global process_method
  process_method = method


def process_path(path: Path, encoding: str, inp_dir: Path, out_dir: Path) -> Tuple[bool, Optional[Tuple[str, Exception]]]:
  global process_method

  try:
    text = path.read_text(encoding)
  except Exception as ex:
    ex_info = (f"File {path.relative_to(inp_dir)} couldn't be read! Skipped.", ex)
    return False, ex_info

  normalized_text = process_method(text)
  changed_anything = normalized_text != text
  del text

  if inp_dir == out_dir and not changed_anything:
    del changed_anything
    return False, None

  new_path_with_txt_file = out_dir / path.relative_to(inp_dir)

  try:
    new_path_with_txt_file.parent.mkdir(parents=True, exist_ok=True)
    new_path_with_txt_file.write_text(normalized_text, encoding=encoding)
  except Exception as ex:
    del normalized_text
    ex_info = (f"File {path.relative_to(inp_dir)} couldn't be written! Skipped.", ex)
    return False, ex_info

  del normalized_text
  return changed_anything, None
