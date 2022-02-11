import re


def normalize_am_and_pm(text: str) -> str:
  text = text.replace("p.m.", "p m")
  text = text.replace("a.m.", "a m")
  return text


CAPITAL_LETTERS_WITH_DOT_AND_ALPHANUM_AFTERWARDS = re.compile(r"([^A-Z])([A-Z])\.(\w)")
CAPITAL_LETTERS_WITH_DOT_AND_NOT_ALPHANUM_AFTERWARDS = re.compile(r"([^A-Z])([A-Z])\.(\W)")


def remove_dot_after_single_capital_letters(text: str) -> str:
  while text != CAPITAL_LETTERS_WITH_DOT_AND_ALPHANUM_AFTERWARDS.sub(r"\1\2 \3", text):
    text = CAPITAL_LETTERS_WITH_DOT_AND_ALPHANUM_AFTERWARDS.sub(r"\1\2 \3", text)
  while text != CAPITAL_LETTERS_WITH_DOT_AND_NOT_ALPHANUM_AFTERWARDS.sub(r"\1\2\3", text):
    text = CAPITAL_LETTERS_WITH_DOT_AND_NOT_ALPHANUM_AFTERWARDS.sub(r"\1\2\3", text)
  return text

# [a-z]\.[a-z]
# [b-dfghj-oq-ux-z]\.[a-z]


def remove_dot_after_single_small_letters(text: str) -> str:
  pass
