from pathlib import Path

from english_text_normalization.auxiliary_methods.search_pattern_in_books import (
  process_matches, search_pattern_in_all_books,
  search_pattern_in_all_books_and_name_with_first_letter_capital_rest_small_before,
  search_pattern_in_all_books_and_word_after, search_pattern_in_all_books_and_word_before,
  search_pattern_in_all_books_and_word_before_and_after)
from english_text_normalization.auxiliary_methods.txt_files_reading import write_in_txt_file


def test_search_pattern_in_all_books():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = r"cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 2)

  assert list(res) == ["Abcdef", "abcdef"]


def test_search_pattern_in_all_books__double_result_cut_out():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = r"cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 1)

  assert list(res) == ["bcde", "bcde"]


def test_search_pattern_in_all_books__pattern_at_beginning_and_end():
  books = [
    "Abcdefg",
    "abcdef",
    "fg",
  ]
  pattern = r"fg"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 2)

  assert list(res) == ["defg", "fg"]


def test_search_pattern_in_all_books__with_new_lines_in_book():
  books = [
    "Abc\ndefg",
    "abcd\nef",
    "ab\ncdefg",
  ]
  pattern = r"cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 3)

  assert list(res) == ["abcd", "cdefg"]


def test_process_matches__cut_out_duplicates():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = r"cd"  # re.compile(r"cd")
  matches = search_pattern_in_all_books(pattern, books, 1)
  res = process_matches(matches)

  assert res == "bcde"


def test_process_matches__sort_alphabetically():
  books = [
    "Abc\ndefg",
    "ab\ncdefg",
    "abcd\nef",
  ]
  pattern = r"cd"  # re.compile(r"cd")
  matches = search_pattern_in_all_books(pattern, books, 3)
  res = process_matches(matches)

  assert res == "abcd\ncdefg"


def test_write_in_txt_file():
  books = [
    "Abc\ndefg",
    "ab\ncdefg",
    "abcd\nef",
  ]
  pattern = "cd"  # re.compile(r"cd")
  matches = search_pattern_in_all_books(pattern, books, 3)
  res = process_matches(matches)
  write_in_txt_file(res, Path("data/test.txt"))


def test_search_pattern_in_all_books_and_word_before_and_after():
  books = [
    "Henry II.",
    "Napoleon II. from France",
    "Henry III. from England",
    "II. HEADLINE"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_word_before_and_after(pattern, books)
  res = list(res)

  assert res == ["Henry II.", "Napoleon II. from", "II. HEADLINE"]


def test_search_pattern_in_all_books_and_word_before_and_after_with_new_lines():
  books = [
    "abc\nHenry II.\ndef",
    "abc\nNapoleon II. from France\ndef",
    "abc\nHenry III. from England\ndef",
    "abc\nII. HEADLINE\ndef"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_word_before_and_after(pattern, books)
  res = list(res)

  assert res == ["Henry II.", "Napoleon II. from", "II. HEADLINE"]


def test_search_pattern_in_all_books_and_word_before():
  books = [
    "Henry II.",
    "Napoleon II. from France",
    "Henry III. from England",
    "II. HEADLINE"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_word_before(pattern, books)
  res = list(res)

  assert res == ["Henry II.", "Napoleon II."]


def test_search_pattern_in_all_books_and_word_before_without_dot():
  books = [
    "Henry II",
    "Napoleon II from France",
    "Henry III from England",
    "II HEADLINE"
  ]
  pattern = r"II"
  res = search_pattern_in_all_books_and_word_before(pattern, books)
  res = list(res)

  assert res == ["Henry II", "Napoleon II"]


def test_search_pattern_in_all_books_and_word_before_with_new_lines():
  books = [
    "abc\nHenry II.\ndef",
    "abc\nNapoleon II. from France\ndef",
    "abc\nHenry III. from England\ndef",
    "abc\nII. HEADLINE\ndef"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_word_before(pattern, books)
  res = list(res)

  assert res == ["Henry II.", "Napoleon II."]


def test_search_pattern_in_all_books_and_word_before__with_new_lines__without_dots():
  books = [
    "abc\nHenry II\ndef",
    "abc\nNapoleon II from France\ndef",
    "abc\nHenry III from England\ndef",
    "abc\nII HEADLINE\ndef"
  ]
  pattern = r"II"
  res = search_pattern_in_all_books_and_word_before(pattern, books)
  res = list(res)

  assert res == ["Henry II", "Napoleon II"]


def test_search_pattern_in_all_books_and_word_after():
  books = [
    "Henry II.",
    "Napoleon II. from France",
    "Henry III. from England",
    "II. HEADLINE"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_word_after(pattern, books)
  res = list(res)

  assert res == [" II. from", "II. HEADLINE"]


def test_search_pattern_in_all_books_and_word_after_with_new_lines():
  books = [
    "abc\nHenry II.\ndef",
    "abc\nNapoleon II. from France\ndef",
    "abc\nHenry III. from England\ndef",
    "abc\nII. HEADLINE\ndef"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_word_after(pattern, books)
  res = list(res)

  assert res == [" II. from", "II. HEADLINE"]


def test_search_pattern_in_all_books_and_name_with_first_letter_capital_rest_small_before():
  books = [
    "abc\nHENRY II.\ndef",
    "abc\nHenry II.\ndef",
    "abc\nNapoleon II. from France\ndef",
    "abc\nHenry III. from England\ndef",
    "abc\nII. HEADLINE\ndef"
  ]
  pattern = r"II\."
  res = search_pattern_in_all_books_and_name_with_first_letter_capital_rest_small_before(
    pattern, books)
  res = list(res)

  assert res == ["Henry II.", "Napoleon II."]
