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
