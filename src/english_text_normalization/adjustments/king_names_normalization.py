import re
from typing import Iterable

from english_text_normalization.auxiliary_methods.txt_files_reading import \
    get_list_out_of_txt_file

KING_NUMBER_MAPPINGS_WITHOUT_DOT = [
  # (re.compile(r" the I[\.st]?(\W)"), " the first"),
  (re.compile(r" the II[\.nd]{0,3}(\W)"), r" the second\1"),
  (re.compile(r" the III[\.rd]{0,3}(\W)"), r" the third\1"),
  (re.compile(r" the IV[\.th]{0,3}(\W)"), r" the fourth\1"),
  (re.compile(r" the V[\.th]{0,3}(\W)"), r" the fifth\1"),
  (re.compile(r" the VI[\.th]{0,3}(\W)"), r" the sixth\1"),
  (re.compile(r" the VII[\.th]{0,3}(\W)"), r" the seventh\1"),
  (re.compile(r" the VIII[\.th]{0,3}(\W)"), r" the eighth\1"),
  (re.compile(r" the IX[\.th]{0,3}(\W)"), r" the ninth\1"),
  (re.compile(r" the X[\.th]{0,3}(\W)"), r" the tenth\1"),
  (re.compile(r" the XI[\.th]{0,3}(\W)"), r" the eleventh\1"),
  (re.compile(r" the XII[\.th]{0,3}(\W)"), r" the twelfth\1"),
  (re.compile(r" the XIII[\.th]{0,3}(\W)"), r" the thirteenth\1"),
  (re.compile(r" the XIV[\.th]{0,3}(\W)"), r" the fourteenth\1"),
  (re.compile(r" the XV[\.th]{0,3}(\W)"), r" the fifteenth\1"),
  (re.compile(r" the XVI[\.th]{0,3}(\W)"), r" the sixteenth\1"),
  (re.compile(r" the XVII[\.th]{0,3}(\W)"), r" the seventeenth\1"),
  (re.compile(r" the XVIII[\.th]{0,3}(\W)"), r" the eighteenth\1"),
  (re.compile(r" the XIX[\.th]{0,3}(\W)"), r" the nineteenth\1"),
  (re.compile(r" the XX[\.th]{0,3}(\W)"), r" the twentieth\1")
]


def normalize_king_names_general(text: str, king_names: Iterable[str], max_number: int = 20) -> str:
  text = add_the_between_king_name_and_roman_numeral(text, king_names)
  for roman_numeral in KING_NUMBER_MAPPINGS_WITHOUT_DOT[::-1]:
    text = roman_numeral[0].sub(roman_numeral[1], text)
  return text


def add_the_between_king_name_and_roman_numeral(text: str, king_names: Iterable[str]) -> str:
  king_names_conc_with_or = "|".join(king_names)
  king_name_plus_roman_numeral = re.compile(rf"({king_names_conc_with_or}) ([XVI]{{2,5}})\.?")
  text = king_name_plus_roman_numeral.sub(r"\1 the \2", text)
  return text


def normalize_our_king_names(text: str) -> str:
  king_names = get_list_out_of_txt_file("data/name_corpus.txt")
  text = normalize_king_names_general(text, king_names)
  return text
