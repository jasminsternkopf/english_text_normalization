from argparse import ArgumentParser, Namespace
from logging import Logger
from pathlib import Path
from typing import Callable, cast

from english_text_normalization.auxiliary_methods.operations import (build_normalizer,
                                                                     get_valid_operations)
from english_text_normalization_cli.globals import ExecutionResult
from english_text_normalization_cli.helper import (parse_codec, parse_existing_file,
                                                   parse_non_empty_or_whitespace, parse_path)


def get_file_normalizing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command normalizes English text."
  parser.add_argument("file", type=parse_existing_file, metavar="FILE",
                      help="text file")
  parser.add_argument("operations", type=parse_non_empty_or_whitespace, metavar="OPERATION",
                      choices=get_valid_operations(), nargs="+", help="operations to apply; order will be considered; same operation can be applied multiple times")
  parser.add_argument("-e", "--encoding", type=parse_codec,
                      default="UTF-8", help="encoding of the texts")
  parser.add_argument("-o", "--output", type=parse_path, metavar="OUTPUT",
                      help="custom output path", default=None)
  return file_normalize_ns


def file_normalize_ns(ns: Namespace, logger: Logger, flogger: Logger) -> ExecutionResult:
  inp_file = cast(Path, ns.file)

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
