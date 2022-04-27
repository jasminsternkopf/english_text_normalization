from argparse import ArgumentParser, Namespace
from typing import Callable

from english_text_normalization.auxiliary_methods.operations import (
  get_operations_and_descriptions, get_valid_operations)


def get_operations_listing_parser(parser: ArgumentParser) -> Callable[[str, str], None]:
  parser.description = "This command lists available operations that can be applied to texts."
  parser.add_argument("-p", "--pipeline", type=str, metavar="OPERATION",
                      choices=get_valid_operations(), nargs="*", help="show only these operations from a pipeline", default=[])
  return list_operations_ns


def list_operations_ns(ns: Namespace):
  ops_dsc = dict(get_operations_and_descriptions())
  if len(ns.pipeline) > 0:
    show_ops = ns.pipeline
  else:
    show_ops = list(ops_dsc.keys())

  for nr, op in enumerate(show_ops, start=1):
    print(f"{nr}. \"{op}\" -> {ops_dsc[op]}")
