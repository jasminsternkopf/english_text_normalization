import argparse
import logging
import sys
from argparse import ArgumentParser
from importlib.metadata import version
from logging import getLogger
from pathlib import Path
from typing import Callable, Generator, List, Tuple

from english_text_normalization_cli.file_text_normalization import get_file_normalizing_parser
from english_text_normalization_cli.folder_text_normalization import get_folder_normalizing_parser
from english_text_normalization_cli.operations_listing import get_operations_listing_parser

__version__ = version("english-text-normalization")

Parsers = Generator[Tuple[str, str, Callable], None, None]

INVOKE_HANDLER_VAR = "invoke_handler"


def formatter(prog):
  return argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=40)

def _init_parser():
  main_parser = ArgumentParser(
    formatter_class=formatter,
    description="This program provides methods normalize English text.",
  )
  main_parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
  subparsers = main_parser.add_subparsers(help="description")

  methods: Parsers = (
    ("normalize-file", "normalize text files",
     get_file_normalizing_parser),
    ("normalize-folder", "normalize text folders",
     get_folder_normalizing_parser),
    ("list-operations", "list operations",
     get_operations_listing_parser),
  )

  for command, description, method in methods:
    method_parser = subparsers.add_parser(
      command, help=description, formatter_class=formatter)
    method_parser.set_defaults(**{
      INVOKE_HANDLER_VAR: method(method_parser),
    })

  return main_parser


def configure_logger(productive: bool) -> None:
  loglevel = logging.INFO if productive else logging.DEBUG
  main_logger = getLogger()
  main_logger.setLevel(loglevel)
  main_logger.manager.disable = logging.NOTSET
  if len(main_logger.handlers) > 0:
    console = main_logger.handlers[0]
  else:
    console = logging.StreamHandler()
    main_logger.addHandler(console)

  logging_formatter = logging.Formatter(
    '[%(asctime)s.%(msecs)03d] (%(levelname)s) %(message)s',
    '%Y/%m/%d %H:%M:%S',
  )
  console.setFormatter(logging_formatter)
  console.setLevel(loglevel)


def parse_args(args: List[str], productive: bool = False):
  configure_logger(productive)
  logger = getLogger(__name__)
  logger.debug("Received args:")
  logger.debug(args)
  parser = _init_parser()
  if len(args) == 0:
    parser.print_help()
    return

  received_args = parser.parse_args(args)
  params = vars(received_args)

  if INVOKE_HANDLER_VAR in params:
    invoke_handler: Callable[[ArgumentParser], None] = params.pop(INVOKE_HANDLER_VAR)
    invoke_handler(received_args)
  else:
    parser.print_help()


def run(productive: bool):
  arguments = sys.argv[1:]
  parse_args(arguments, productive and not debug_file_exists())


def run_prod():
  run(True)


def debug_file_exists():
  return Path("debug").is_file()


if __name__ == "__main__":
  run(not __debug__)
