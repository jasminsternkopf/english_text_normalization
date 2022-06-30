from unidecode import unidecode_expect_ascii
import pickle
from pathlib import Path
from typing import Callable, List

from english_text_normalization.adjustments.abbreviations import expand_abbreviations
from english_text_normalization.adjustments.emails import normalize_emails_and_at
from english_text_normalization.adjustments.king_names_normalization import \
  normalize_king_name_followed_by_roman_numeral
from english_text_normalization.adjustments.layout_normalization import (
  add_dot_after_headings, normalize_three_and_four_dots, remove_double_hyphen_before_or_after_colon,
  remove_equal_sign, remove_linebreaks, remove_quotation_marks_when_used_as_itemization,
  remove_repeated_spaces, remove_stars, remove_underscore_characters, replace_four_hyphens_by_two,
  replace_whitespace_with_space)
from english_text_normalization.adjustments.money_normalization import \
  normalize_pounds_shillings_and_pence
from english_text_normalization.adjustments.month_normalization import write_out_month_abbreviations
from english_text_normalization.adjustments.normalization_of_certain_words_and_abbr import (
  geo_to_george, normalize_today_tomorrow_and_tonight, remove_sic, replace_eg_with_for_example,
  replace_etc_with_et_cetera, replace_ie_with_that_is, replace_no_with_number,
  replace_nos_with_numbers)
from english_text_normalization.adjustments.normalize_degrees import (
  normalize_degrees_minutes_and_seconds, normalize_temperatures_general)
from english_text_normalization.adjustments.numbers import (
  expand_and_a_half, normalize_numbers, normalize_second_and_third_when_abbr_with_d)
from english_text_normalization.adjustments.other import (
  add_space_around_dashes, remove_whitespace_before_sentence_punctuation)
from english_text_normalization.adjustments.remove_dots_that_are_not_end_of_sentence import (
  normalize_am_and_pm, remove_dot_after_single_capital_letters)
from english_text_normalization.adjustments.unit_abbreviations_normalization import \
  normalize_all_units
from english_text_normalization.adjustments.write_out_special_characters import (
  normalize_percent, replace_and_sign_with_word_and, replace_hyphen_between_numbers_with_to)
from english_text_normalization.auxiliary_methods.txt_files_reading import get_text_files


def create_pickle_containing_all_books(folder: Path):
  paths = get_text_files(folder)
  books: List[str] = []
  for path in paths:
    book = path.read_text()
    books.append(book)
  with open('all_books.pickle', 'wb') as file:
    pickle.dump(books, file)


def execute_pipeline(word: str, methods: List[Callable[[str], str]]) -> str:
  result = word
  for method in methods:
    assert isinstance(method, Callable)
    result = method(result)
    assert isinstance(result, str)
  return result


def strip(text: str) -> str:
  return text.strip()


def general_pipeline(text: str) -> str:
  text = execute_pipeline(
    text,
    (
      add_dot_after_headings,
      remove_quotation_marks_when_used_as_itemization,
      remove_linebreaks,
      # remove_numbers_in_square_brackets,
      # remove_illustrations,
      normalize_emails_and_at,
      remove_underscore_characters,
      remove_equal_sign,
      add_space_around_dashes,
      replace_ie_with_that_is,
      replace_eg_with_for_example,
      replace_etc_with_et_cetera,  # unterscheidung groß/kleinbuchstabe danach?
      replace_nos_with_numbers,
      replace_no_with_number,
      geo_to_george,
      write_out_month_abbreviations,
      normalize_today_tomorrow_and_tonight,
      normalize_king_name_followed_by_roman_numeral,
      normalize_am_and_pm,
      normalize_pounds_shillings_and_pence,
      normalize_temperatures_general,
      normalize_degrees_minutes_and_seconds,
      normalize_all_units,
      normalize_percent,
      expand_and_a_half,
      # normalize_fractions
      replace_hyphen_between_numbers_with_to,
      normalize_second_and_third_when_abbr_with_d,  # abändern, allgemeiner machen
      # remove_colon_in_digital_time_format(text) # ist oft bibelstelle
      normalize_numbers,
      expand_abbreviations,
      remove_dot_after_single_capital_letters,
      replace_and_sign_with_word_and,
      remove_double_hyphen_before_or_after_colon,
      normalize_three_and_four_dots,
      replace_four_hyphens_by_two,
      add_space_around_dashes,
      remove_sic,
      remove_stars,
      replace_whitespace_with_space,
      remove_repeated_spaces,
      remove_whitespace_before_sentence_punctuation,
      strip,
      unidecode_expect_ascii,
    )
  )

  return text


# alles in [] wegcutten \[[^I\dFGS_g]
