import re

ONE_POUND_EXPECT_SHILLINGS_AFTERWARDS = re.compile(r" L\.? ?1,?( \d)")
ONE_POUND = re.compile(r" L\.? ?1(\W\W)")
POUNDS_WITH_DOT_AFTER_NUMBER = re.compile(r" L\.? ?(\d+[\d\.,]*)\.(\W)")
POUNDS_WITH_COMMA_AFTER_NUMBER = re.compile(r" L\.? ?(\d+[\d\.,]*)\,(\W)")
POUNDS = re.compile(r" L\.? ?(\d+[\d\.,]*)(\W)")

SHILLINGS_AND_PENCE_WITHOUT_DOT = re.compile(r" (\d{1,2}) ?s,? (\d{1,6}) ?d(\W)")
#SHILLINGS_AND_PENCE_WITHOUT_DOT = re.compile(r" (\d{1,2}) ?s,? ([\d\-/]{1,6}) ?d(\W)")
#SHILLINGS_AND_PENCE_WITH_DOT = re.compile(r" (\d{1,2}) ?s\.,? ?([\d\-/]{1,6}) ?d\.(\W)")
SHILLINGS_AND_PENCE_WITH_DOT = re.compile(r" (\d{1,2}) ?s\.,? ?(\d{1,6}) ?d\.(\W)")

ONE_SHILLING = re.compile(r" 1 ?s[\., ]{1,3}")
SHILLINGS = re.compile(r" (\d{1,2}) ?s[\., ]{1,3}")


ONE_PENNY = re.compile(r" 1 ?d\.?(\W)")
AND_A_HALF_PENCE = re.compile(r"\-?1/2 ?d\.?(\W)")
MORE_THAN_FOUR_PENCE = re.compile(r"([04-9]) ?d\.?(\W)")
# 2d and 3d often stand for second and third, with dot after them when at the end of a sentence.


def normalize_pounds(text: str) -> str:
  text = ONE_POUND_EXPECT_SHILLINGS_AFTERWARDS.sub(r" one pound\1", text)
  text = ONE_POUND.sub(r" one pound\1", text)
  text = POUNDS_WITH_DOT_AFTER_NUMBER.sub(r" \1 pounds\2", text)
  text = POUNDS_WITH_COMMA_AFTER_NUMBER.sub(r" \1 pounds\2", text)
  text = POUNDS.sub(r" \1 pounds\2", text)
  return text


def normalize_shillings_and_pounds_without_dots(text: str) -> str:
  text = SHILLINGS_AND_PENCE_WITHOUT_DOT.sub(r" \1 shillings and \2 pence\3", text)
  return text


def normalize_shillings_and_pounds_with_dots(text: str) -> str:
  text = SHILLINGS_AND_PENCE_WITH_DOT.sub(r" \1 shillings and \2 pence\3", text)
  return text


def normalize_shillings(text: str) -> str:
  text = ONE_SHILLING.sub(r" one shilling ", text)
  text = SHILLINGS.sub(r" \1 shillings ", text)
  return text


def normalize_pence(text: str) -> str:
  text = ONE_PENNY.sub(r" one penny\1", text)
  text = AND_A_HALF_PENCE.sub(r" and a half pence\1", text)
  text = MORE_THAN_FOUR_PENCE.sub(r"\1 pence\2", text)
  return text


def normalize_pounds_shillings_and_pence(text: str) -> str:
  text = normalize_pounds(text)
  text = normalize_shillings_and_pounds_with_dots(text)
  text = normalize_shillings_and_pounds_without_dots(text)
  text = normalize_shillings(text)
  text = normalize_pence(text)
  return text
