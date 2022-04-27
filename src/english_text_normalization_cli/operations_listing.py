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

def get_operations_listing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command lists available operations that can be applied to texts."
  return list_operations_ns


def list_operations_ns(ns: Namespace):
  for op, descr in get_operations_and_descriptions():
    print(f"\"{op}\" -> {descr}")
