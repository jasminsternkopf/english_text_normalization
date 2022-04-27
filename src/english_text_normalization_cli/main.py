from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Callable, cast

VALID_OPERATIONS = {
  "general": "General methods",
  "abbr": "Expand abbreviations",
}


def init_normalizing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command normalizes English text."
  parser.add_argument("directory", type=Path, metavar="directory",
                      help="directory containing texts")
  parser.add_argument("operations", type=str, metavar="operations",
                      choices=list(VALID_OPERATIONS.keys()), nargs="+", help="operations to apply; order will be considered; same operation can be applied multiple times")
  parser.add_argument("--output-directory", type=Path, metavar="PATH",
                      help="custom directory to output normalized texts (existing texts will be overwritten); defaults to the input directory if it is not set", default=None)
  return normalize_ns


def normalize_ns(ns: Namespace):
  if not cast(Path, ns.directory).is_dir():
    raise ValueError("Parameter 'directory': Directory does not exist!")


def init_sentence_extraction_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command separates sentences of English text."
  parser.add_argument("directory", type=Path, metavar="directory",
                      help="directory containing texts")
  parser.add_argument("--output-directory", type=Path, metavar="PATH",
                      help="custom directory to output texts (existing texts will be overwritten); defaults to the input directory if it is not set", default=None)
  return extract_sentences_ns


def extract_sentences_ns(ns: Namespace):
  if not cast(Path, ns.directory).is_dir():
    raise ValueError("Parameter 'directory': Directory does not exist!")


def get_operations_listing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command lists available operations that can be applied to texts."
  return list_operations_ns


def list_operations_ns(ns: Namespace):
  for k, v in VALID_OPERATIONS.items():
    print(f"{k}: {v}")
