import pickle
from pathlib import Path
from typing import List

from english_text_normalization.adjustments.abbreviations import \
    expand_abbreviations
from english_text_normalization.adjustments.emails import \
    normalize_emails_and_at
from english_text_normalization.adjustments.king_names_normalization import \
    normalize_our_king_names
from english_text_normalization.adjustments.layout_normalization import (
    add_dot_after_headings, insert_space_before_and_after_double_hyphen,
    normalize_three_and_four_dots, remove_double_hyphen_before_or_after_colon,
    remove_equal_sign, remove_linebreaks,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_stars, remove_underscore_characters, replace_four_hyphens_by_two)
from english_text_normalization.adjustments.money_normalization import \
    normalize_pounds_shillings_and_pence
from english_text_normalization.adjustments.month_normalization import \
    write_out_month_abbreviations
from english_text_normalization.adjustments.normalizaton_of_certain_words_and_abbr import (
    geo_to_george, normalize_today_and_tomorrow, remove_sic,
    replace_eg_with_for_example, replace_etc_with_et_cetera,
    replace_ie_with_that_is, replace_no_with_number, replace_nos_with_numbers)
from english_text_normalization.adjustments.normalize_degrees import (
    normalize_degrees_minutes_and_seconds, normalize_temperatures_general)
from english_text_normalization.adjustments.numbers import (
    expand_and_a_half, normalize_numbers,
    normalize_second_and_third_when_abbr_with_d)
from english_text_normalization.adjustments.remove_dots_that_are_not_end_of_sentence import (
    normalize_am_and_pm, remove_dot_after_single_capital_letters)
from english_text_normalization.adjustments.unit_abbreviations_normalization import \
    normalize_all_units
from english_text_normalization.adjustments.write_out_special_characters import (
    normalize_percent, replace_and_sign_with_word_and,
    replace_hyphen_between_numbers_with_to)
from english_text_normalization.auxiliary_methods.txt_files_reading import \
    get_text_files
from english_text_normalization.sentence_extraction import \
    extract_sentences_of_all_books


def create_pickle_containing_all_books(folder: Path):
  paths = get_text_files(folder)
  books: List[str] = []
  for path in paths:
    book = path.read_text()
    books.append(book)
  with open('all_books.pickle', 'wb') as file:
    pickle.dump(books, file)


def general_pipeline(text: str) -> str:
  text = add_dot_after_headings(text)
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_linebreaks(text)
  #text = remove_numbers_in_square_brackets(text)
  #text = remove_illustrations(text)
  text = normalize_emails_and_at(text)
  text = remove_underscore_characters(text)
  text = remove_equal_sign(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = replace_ie_with_that_is(text)
  text = replace_eg_with_for_example(text)
  text = replace_etc_with_et_cetera(text)  # untesrcheidund groß/kleinbuchstabe danach?
  text = replace_nos_with_numbers(text)
  text = replace_no_with_number(text)
  text = geo_to_george(text)
  text = write_out_month_abbreviations(text)
  text = normalize_today_and_tomorrow(text)
  text = normalize_our_king_names(text)
  text = normalize_am_and_pm(text)
  text = normalize_pounds_shillings_and_pence(text)
  text = normalize_temperatures_general(text)
  text = normalize_degrees_minutes_and_seconds(text)
  text = normalize_all_units(text)
  text = normalize_percent(text)
  text = expand_and_a_half(text)
  # text = normalize_fractions(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_second_and_third_when_abbr_with_d(text)  # abändern, allgemeiner machen
  # text = remove_colon_in_digital_time_format(text) ist oft bibelstelle
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = remove_dot_after_single_capital_letters(text)
  text = replace_and_sign_with_word_and(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = normalize_three_and_four_dots(text)
  text = replace_four_hyphens_by_two(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_sic(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
# alles in [] wegcutten \[[^I\dFGS_g]



if __name__ == "__main__":
  # create_pickle_containing_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"))
  extract_sentences_of_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"),
                                 ("../DATA/data/librispeech-lm-corpus/sentencewise_corpus"))
