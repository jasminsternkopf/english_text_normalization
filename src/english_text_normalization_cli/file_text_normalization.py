from argparse import ArgumentParser, Namespace
from functools import partial
from logging import getLogger
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Callable, Tuple, cast

from english_text_normalization.auxiliary_methods.operations import (build_normalizer,
                                                                     get_valid_operations)
from english_text_normalization.auxiliary_methods.txt_files_reading import get_text_files


def get_file_normalizing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command normalizes English text."
  parser.add_argument("file", type=Path, metavar="FILE-PATH",
                      help="text file")
  parser.add_argument("operations", type=str, metavar="operations",
                      choices=get_valid_operations(), nargs="+", help="operations to apply; order will be considered; same operation can be applied multiple times")
  parser.add_argument("-e", "--encoding", type=str, default="UTF-8", help="encoding of the texts")
  parser.add_argument("-o", "--output", type=Path, metavar="OUTPUT-PATH",
                      help="custom output path", default=None)
  return file_normalize_ns


def file_normalize_ns(ns: Namespace):
  logger = getLogger(__name__)
  inp_file = cast(Path, ns.file)
  if not inp_file.is_file():
    raise ValueError("Parameter 'file': File does not exist!")

  try:
    text = inp_file.read_text(ns.encoding)
  except Exception as ex:
    logger.error(f"File \"{inp_file.absolute()}\" couldn't be read!")
    logger.debug(ex)
    return False, False

  normalizer = build_normalizer(ns.operations)
  normalized_text = normalizer(text)

  changed_anything = normalized_text != text
  del text

  if not changed_anything:
    logger.info("Didn't changed anything!")
    return True, False

  output_path = inp_file
  if ns.output is not None:
    output_path = ns.output
  try:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(normalized_text, ns.encoding)
  except Exception as ex:
    logger.error(f"File \"{output_path.absolute()}\" couldn't be written!")
    logger.debug(ex)
    return False, False

  #logger.info("Everything was successful!")
  return True, True
