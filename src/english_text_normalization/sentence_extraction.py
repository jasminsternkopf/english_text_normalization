import re
from pathlib import Path
from typing import Callable

from english_text_normalization.auxiliary_methods.txt_files_reading import \
    get_text_files


def extract_sentences_of_all_books(folder: Path, new_folder: Path, normalizer: Callable[[str], str]) -> str:
  paths = get_text_files(folder)
  for path in paths:
    book = path.read_text()
    sentencewise_book = extract_sentences(book, normalizer)
    new_path_with_txt_file = new_folder / path.relative_to(folder)
    new_path = new_path_with_txt_file.parent
    if not new_path.exists():
      new_path.mkdir(parents=True)
    new_path_with_txt_file.write_text(sentencewise_book, encoding="UTF-8")


SENTENCE_ENDS = [".", "?", "!"]
SENTENCE_ENDS = [re.escape(x) for x in SENTENCE_ENDS]
#SENTENCE_ENDS_AND_CAPITAL_LETTER = [re.compile(rf"({end}\"?)(?: |\-\-|\.\.\.)(\"?[A-Z])") for end in SENTENCE_ENDS]
SENTENCE_ENDS_AND_CAPITAL_LETTER = [re.compile(rf"({end}\"?) (?:-- )?(\"?[A-Z])") for end in SENTENCE_ENDS]


def extract_sentences(text: str, normalizer: Callable[[str], str]) -> str:
  text = normalizer(text)
  for sentence_end in SENTENCE_ENDS_AND_CAPITAL_LETTER:
    text = sentence_end.sub(r"\1\n\2", text)
  text = remove_quotation_marks_in_line_if_uneven_number_of_them(text)
  return text


def remove_quotation_marks_in_line_if_uneven_number_of_them(text: str) -> str:
  sentences = text.split("\n")
  new_sentences = []
  for sentence in sentences:
    if sentence.count("\"") % 2 == 1:
      sentence = sentence.replace("\"", "")
    new_sentences.append(sentence)
  new_sentences_single_string = "\n".join(new_sentences)
  return new_sentences_single_string
