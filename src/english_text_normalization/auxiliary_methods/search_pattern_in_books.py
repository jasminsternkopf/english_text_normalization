import re
from typing import Iterable, Iterator


def search_pattern_in_all_books(pattern: str, books: Iterable[str], chars_before_and_after: int = 5):
  #pattern = re.escape(pattern)
  pattern_and_span = re.compile(
    rf".{{0,{chars_before_and_after}}}{pattern}.{{0,{chars_before_and_after}}}")
  for book in books:
    matches = pattern_and_span.findall(book)
    for match in matches:
      yield match


def search_pattern_in_all_books_and_word_before_and_after(pattern: str, books: Iterable[str]):
  #pattern = re.escape(pattern)
  pattern_and_word_before_and_after = re.compile(
    rf"(?:\w+ |^){pattern}(?: \w+|$)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      yield match


def search_pattern_in_all_books_and_word_before(pattern: str, books: Iterable[str]):
  pattern_and_word_before_and_after = re.compile(
    rf"(?:\w+ ){pattern}(?: |$)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      if match[-1] == " ":
        yield match[:-1]
      else:
        yield match


def search_pattern_in_all_books_and_name_before(pattern: str, books: Iterable[str]):
  pattern_and_word_before_and_after = re.compile(
    rf"(?:[A-Z]\w* ){pattern}(?: |$)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      if match[-1] == " ":
        yield match[:-1]
      else:
        yield match


def search_pattern_in_all_books_and_name_with_first_letter_capital_rest_small_before(pattern: str, books: Iterable[str]):
  pattern_and_word_before_and_after = re.compile(
    rf"(?:[A-Z][a-z]+ ){pattern}(?: |$)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      if match[-1] == " ":
        yield match[:-1]
      else:
        yield match


def search_pattern_in_all_books_and_word_after(pattern: str, books: Iterable[str]):
  pattern_and_word_before_and_after = re.compile(
    rf"(?: |^){pattern}(?: \w+)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      if match[-1] == " ":
        yield match[:-1]
      else:
        yield match


def process_matches(matches: Iterator):
  matches = sorted(set(matches))
  matches_linewise = "\n".join(matches)
  return matches_linewise



