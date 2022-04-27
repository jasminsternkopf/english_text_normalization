from argparse import ArgumentParser, Namespace
from functools import partial
from logging import getLogger
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Callable, Iterable, List, cast

from tqdm import tqdm

from english_text_normalization import *
from english_text_normalization.auxiliary_methods.operations import (build_normalizer,
                                                                     get_valid_operations)
from english_text_normalization.auxiliary_methods.txt_files_reading import get_text_files


def get_normalizing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command normalizes English text."
  parser.add_argument("directory", type=Path, metavar="directory",
                      help="directory containing texts")
  parser.add_argument("operations", type=str, metavar="operations",
                      choices=get_valid_operations(), nargs="+", help="operations to apply; order will be considered; same operation can be applied multiple times")
  parser.add_argument("-o", "--output-directory", type=Path, metavar="PATH",
                      help="custom directory to output normalized texts (existing texts will be overwritten); defaults to the input directory if it is not set", default=None)
  parser.add_argument("-e", "--encoding", type=str, default="UTF-8", help="encoding of the texts")
  parser.add_argument("-j", "--n-jobs", metavar='N', type=int,
                      choices=range(1, cpu_count() + 1), default=cpu_count(), help="amount of parallel cpu jobs")
  parser.add_argument("-c", "--chunksize", type=int, metavar="NUMBER",
                      help="amount of files to chunk into one job", default=10)
  parser.add_argument("-mt", "--maxtasksperchild", type=int, metavar="NUMBER",
                      help="amount of tasks per child", default=None)
  return normalize_ns


def normalize_ns(ns: Namespace):
  logger = getLogger(__name__)
  inp_dir = cast(Path, ns.directory)
  if not inp_dir.is_dir():
    raise ValueError("Parameter 'directory': Directory does not exist!")

  output_directory = inp_dir
  if ns.output_directory is not None:
    output_directory = cast(Path, ns.output_directory)
    if output_directory.is_file():
      raise ValueError("Parameter 'output_directory': Path is a file!")

  paths = list(tqdm(get_text_files(inp_dir), desc="Collecting text files", unit="f"))
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
    iterator = tqdm(iterator, total=len(paths), desc="Normalizing files", unit="f")
    result = list(iterator)

  if all(result):
    logger.info("Everything was successfull!")
  else:
    logger.warning("Not everything was successfull!")


process_method: Callable[[str], str] = None


def __init_pool_prepare_cache_mp(method: Callable[[str], str]) -> None:
  global process_method
  process_method = method


def process_path(path: Path, encoding: str, inp_dir: Path, out_dir: Path) -> bool:
  global process_method
  logger = getLogger(__name__)

  try:
    text = path.read_text(encoding)
  except Exception as ex:
    logger.error(f"File {path.relative_to(inp_dir)} couldn't be read! Skipped.")
    logger.debug(ex)
    return False

  normalized_text = process_method(text)
  del text

  new_path_with_txt_file = out_dir / path.relative_to(inp_dir)

  try:
    new_path_with_txt_file.parent.mkdir(parents=True, exist_ok=True)
    new_path_with_txt_file.write_text(normalized_text, encoding=encoding)
  except Exception as ex:
    logger.error(f"File {path.relative_to(inp_dir)} couldn't be written! Skipped.")
    logger.debug(ex)
    return False

  del normalized_text
  del logger
  return True
