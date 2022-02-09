import os
from collections import OrderedDict
from pathlib import Path
from typing import Generator, Iterable, List, Optional
from typing import OrderedDict as OrderedDictType
from typing import Set, Tuple

from english_text_normalization.auxiliary_methods.search_pattern_in_books import \
    write_in_txt_file

TXT_FILE_TYPE = ".txt"


def get_text_files(folder: Path) -> Generator[Path, None, None]:
  return get_files_dict(folder, filetypes={TXT_FILE_TYPE})


def get_files_dict(folder: Path, filetypes: Set[str]) -> Generator[Path, None, None]:
  filetypes_lower = {ft.lower() for ft in filetypes}
  all_files = get_all_files_in_all_subfolders(folder)
  resulting_files = (file
                     for file in all_files if file.suffix.lower() in filetypes_lower
                     )
  return resulting_files


def get_all_files_in_all_subfolders(dir: Path) -> Generator[Path, None, None]:
  for root, _, files in os.walk(dir):
    for name in files:
      file_path = Path(root) / name
      yield file_path


def get_list_out_of_txt_file(filename: str) -> List[str]:
  with open(filename) as f:
    lines = f.readlines()
  lines = [line[:-1] if line[-1] == "\n" else line for line in lines]
  return lines


def get_str_out_of_txt_file(filename: str, sep: str = "\n") -> List[str]:
  with open(filename) as f:
    lines = f.readlines()
  if sep != "\n":
    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]
    single_str = sep.join(lines)
  else:
    single_str = "".join(lines)
  return single_str


def dump_iterable_in_txt_file(text_as_iterable: Iterable[str], path: Path):
  text_as_str = "\n".join(text_as_iterable)
  write_in_txt_file(text_as_str, path)
