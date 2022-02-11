import re

HEADING = re.compile(r"\n([A-Z \"]+)\n")


def add_dot_after_headings(text: str) -> str:
  text = HEADING.sub(r"\n\1.\n", text)
  return text


QUOTATION_MARK_AS_ITEMIZATION_OF_PARAGRAPH = re.compile(r"^\"([^\"]+)$\n\n", flags=re.MULTILINE)


def remove_quotation_marks_when_used_as_itemization(text: str) -> str:
  text = QUOTATION_MARK_AS_ITEMIZATION_OF_PARAGRAPH.sub(r"\1\n\n", text)
  return text


def remove_linebreaks(text: str) -> str:
  text = text.replace("\n", " ")
  return text


SQUARE_BRACKETS_AND_ITS_CONTENTS = re.compile(r"\[[^\]]{0,1000}\]")


def remove_everything_in_square_brackets(text: str) -> str:
  text = SQUARE_BRACKETS_AND_ITS_CONTENTS.sub("", text)
  return text


STAGE_DIRECTIONS = re.compile(r"\[_[^\]]{0,500}_\.\n")

"""
TODO
alles was [] betrifft:
nur entfernen wenn mitten in einem Satz (z.B. Hallo, [abc] Welt!), ansonsten einfach Klammern entfernen und REst behalten

"""


def remove_stage_directions(text: str) -> str:
  text = STAGE_DIRECTIONS.sub("", text)
  return text


NUMBERS_IN_SQUARE_BRACKETS = re.compile(r"\[\d+\]")


def remove_numbers_in_square_brackets(text: str) -> str:
  text = NUMBERS_IN_SQUARE_BRACKETS.sub("", text)
  return text


ILLUSTRATION = re.compile(r"\[Illustration[^\]]*\]")


def remove_illustrations(text: str) -> str:
  text = ILLUSTRATION.sub("", text)
  return text


def remove_underscore_characters(text: str) -> str:
  text = text.replace("_", "")
  return text


DOUBLE_HYPHEN_NOT_AFTER_CAPITAL_LETTER = re.compile(r"([^A-Z])--")


def insert_space_before_and_after_double_hyphen(text: str) -> str:
  # exception: after capital letter - ist das sinnvoll? TODO
  text = DOUBLE_HYPHEN_NOT_AFTER_CAPITAL_LETTER.sub(r"\1 -- ", text)
  return text


def remove_double_hyphen_before_or_after_colon(text: str) -> str:
  text = text.replace(":--", ": ")
  text = text.replace("--:", ":")
  return text


DIGITAL_TIME = re.compile(r"(\d):(\d\d)")


def remove_colon_in_digital_time_format(text: str) -> str:
  text = DIGITAL_TIME.sub(r"\1 \2", text)
  return text


THREE_POINTS_BETWEEN_SENTENCES = re.compile(r"(\.\"| )\.\.\. (\"{0,1}[A-Z])")
THREE_POINTS_MID_SENTENCE = re.compile(r"\.\.\. ([^A-Z])")


def normalize_three_and_four_dots(text: str) -> str:
  text = text.replace("....", ".")
  text = THREE_POINTS_BETWEEN_SENTENCES.sub(r"\1 \2", text)
  text = THREE_POINTS_MID_SENTENCE.sub(r"\1", text)
  text = text.replace("...", ".")
  return text


def replace_four_hyphens_by_two(text: str) -> str:
  text = text.replace("----", "--")
  return text


def remove_four_hyphens(text: str) -> str:
  text = text.replace("----", "")
  return text


def remove_stars(text: str) -> str:
  text = text.replace("*", "")
  return text


REPEATED_SPACES = re.compile(r" {2,}")


def remove_repeated_spaces(text: str) -> str:
  text = REPEATED_SPACES.sub(" ", text)
  return text


def remove_equal_sign(text: str) -> str:
  # is very rarely used as actual equal sign, much more often in headings or accentuation
  text = text.replace("=", "")
  return text
