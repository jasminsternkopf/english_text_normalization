from argparse import ArgumentParser, Namespace
from functools import partial
from logging import getLogger
from pathlib import Path
from typing import Callable, Iterable, List, cast

from tqdm import tqdm

from english_text_normalization import *
from english_text_normalization.auxiliary_methods.operations import (
  build_normalizer, get_operations_and_descriptions, get_valid_operations)
from english_text_normalization.auxiliary_methods.txt_files_reading import get_text_files
from english_text_normalization.normalization_pipeline import general_pipeline


def get_normalizing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command normalizes English text."
  parser.add_argument("directory", type=Path, metavar="directory",
                      help="directory containing texts")
  parser.add_argument("operations", type=str, metavar="operations",
                      choices=get_valid_operations(), nargs="+", help="operations to apply; order will be considered; same operation can be applied multiple times")
  parser.add_argument("--output-directory", type=Path, metavar="PATH",
                      help="custom directory to output normalized texts (existing texts will be overwritten); defaults to the input directory if it is not set", default=None)
  parser.add_argument("--encoding", type=str, default="UTF-8", help="encoding of the texts")
  return normalize_ns


def normalize_ns(ns: Namespace):
  inp_dir = cast(Path, ns.directory)
  if not inp_dir.is_dir():
    raise ValueError("Parameter 'directory': Directory does not exist!")

  paths = get_text_files(inp_dir)

  output_directory = inp_dir
  if ns.output_directory is not None:
    output_directory = cast(Path, ns.output_directory)
    if output_directory.is_file():
      raise ValueError("Parameter 'output_directory': Path is a file!")

  logger = getLogger(__name__)
  normalizer = build_normalizer(ns.operations)

  for path in tqdm(paths):
    try:
      book = path.read_text(ns.encoding)
    except Exception as ex:
      logger.error(f"File {path.relative_to(inp_dir)} couldn't be read! Skipped.")
      logger.debug(ex)
      continue

    sentencewise_book = normalizer(book)

    new_path_with_txt_file = output_directory / path.relative_to(inp_dir)

    try:
      new_path_with_txt_file.parent.mkdir(parents=True, exist_ok=True)
      new_path_with_txt_file.write_text(sentencewise_book, encoding=ns.encoding)
    except Exception as ex:
      logger.error(f"File {path.relative_to(inp_dir)} couldn't be written! Skipped.")
      logger.debug(ex)
      continue


def get_sentence_extraction_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command separates sentences of English text."
  parser.add_argument("directory", type=Path, metavar="directory",
                      help="directory containing texts (*.txt)")
  parser.add_argument("--output-directory", type=Path, metavar="PATH",
                      help="custom directory to output texts (existing texts will be overwritten); defaults to the input directory if it is not set", default=None)
  parser.add_argument("--encoding", type=str, default="UTF-8", help="encoding of the texts")
  return extract_sentences_ns


def extract_sentences_ns(ns: Namespace):
  inp_dir = cast(Path, ns.directory)
  if not inp_dir.is_dir():
    raise ValueError("Parameter 'directory': Directory does not exist!")

  paths = get_text_files(inp_dir)

  output_directory = inp_dir
  if ns.output_directory is not None:
    output_directory = cast(Path, ns.output_directory)
    if output_directory.is_file():
      raise ValueError("Parameter 'output_directory': Path is a file!")

  logger = getLogger(__name__)
  for path in paths:
    try:
      book = path.read_text(ns.encoding)
    except Exception as ex:
      logger.error(f"File {path.relative_to(inp_dir)} couldn't be read! Skipped.")
      logger.debug(ex)
      continue

    sentencewise_book = extract_sentences(book)

    new_path_with_txt_file = output_directory / path.relative_to(inp_dir)

    try:
      new_path_with_txt_file.parent.mkdir(parents=True, exist_ok=True)
      new_path_with_txt_file.write_text(sentencewise_book, encoding=ns.encoding)
    except Exception as ex:
      logger.error(f"File {path.relative_to(inp_dir)} couldn't be written! Skipped.")
      logger.debug(ex)
      continue


def get_operations_listing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command lists available operations that can be applied to texts."
  return list_operations_ns


def list_operations_ns(ns: Namespace):
  for op, descr in get_operations_and_descriptions():
    print(f"\"{op}\" -> {descr}")
