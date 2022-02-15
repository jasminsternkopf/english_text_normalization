import re


def replace_and_sign_with_word_and(text: str) -> str:
  text = text.replace(" & ", " and ")
  return text


POINT_BEFORE_NUMBER = re.compile(r"·(\d+)")


def normalize_point_before_numbers(text: str) -> str:
  text = POINT_BEFORE_NUMBER.sub(r" point \1", text)
  return text


HYPHEN_BETWEEN_NUMBERS = re.compile(r"(\d+)-(\d+)")


def replace_hyphen_between_numbers_with_to(text):
  text = HYPHEN_BETWEEN_NUMBERS.sub(r"\1 to \2", text)
  return text


PERCENT = re.compile(r"(\d) ?%")


def normalize_percent(text: str) -> str:
  text = PERCENT.sub(r"\1 percent", text)
  return text


def normalize_double_quotation_marks(text: str) -> str:
  text = text.replace("“", "\"")
  text = text.replace("”", "\"")
  return text


UNUSUAL_QUOTATION_MARKS = re.compile(r"‘([^’]{2,2000})’")


def normalize_single_quotation_marks_and_apostrophes(text: str) -> str:
  text = UNUSUAL_QUOTATION_MARKS.sub(r'"\1"', text)
  text = text.replace("’", "'")
  return text


def write_out_plus_when_surrounded_by_space(text: str) -> str:
  text = text.replace(" + ", " plus ")
  return text
