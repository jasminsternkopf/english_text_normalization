from functools import partial
from typing import Callable, Generator, List, Tuple, cast

from english_text_normalization import *
from english_text_normalization.normalization_pipeline import execute_pipeline, general_pipeline

VALID_OPERATIONS = {
  "general": (
    "General methods",
    general_pipeline
  ),
  "sents": (
    "Separate sentences onto a single line",
    extract_sentences
  ),
  "abbr": (
    "Expand abbreviations",
    expand_abbreviations
  ),
  "num": (
    "Normalize numbers",
    normalize_numbers
  ),
  "temps": (
    "Normalize temperatures Celsius and Fahrenheit",
    normalize_temperatures_general
  ),
  "lb": (
    "Remove linebreaks",
    remove_linebreaks
  ),
  "eq": (
    "Remove '=' signs",
    remove_equal_sign
  ),
  "til": (
    "Remove '~' signs",
    remove_tilde
  ),
  "mail": (
    "Normalize e-mail addresses and the '@'-symbol",
    replace_mail_addresses
  ),
  "strip": (
    "Strip whitespace from start and end",
    strip
  ),
  "am-pm": (
    "Normalize a.m./p.m.",
    normalize_am_and_pm
  ),
  "units": (
    "Normalize time, weight and length units",
    normalize_all_units
  ),
  "lower": (
    "Convert everything to lower-case",
    str.lower
  ),
  "upper": (
    "Convert everything to upper-case",
    str.upper
  )
}


def get_valid_operations() -> List[str]:
  return list(VALID_OPERATIONS.keys())


def get_operations_and_descriptions() -> Generator[Tuple[str, str], None, None]:
  for op, (descr, _) in VALID_OPERATIONS.items():
    yield op, descr


def build_normalizer(operations: List[str]) -> Callable[[str], str]:
  methods = list(VALID_OPERATIONS[op][1] for op in operations)
  result = partial(execute_pipeline, methods=methods)
  return result
