import re
from typing import List, Pattern, Tuple

MONTH_MAPPINGS: List[Tuple[Pattern, str]] = [
  (re.compile(r" jan\.", re.IGNORECASE), " January"),
  (re.compile(r" feb\.", re.IGNORECASE), " February"),
  (re.compile(r" mar\.", re.IGNORECASE), " March"),
  (re.compile(r" apr\.", re.IGNORECASE), " April"),
  (re.compile(r" aug\.", re.IGNORECASE), " August"),
  (re.compile(r" sept\.", re.IGNORECASE), " September"),
  (re.compile(r" oct\.", re.IGNORECASE), " October"),
  (re.compile(r" nov\.", re.IGNORECASE), " November"),
  (re.compile(r" dec\.", re.IGNORECASE), " December")
]


def write_out_month_abbreviations(text: str) -> str:
  for month in MONTH_MAPPINGS:
    text = month[0].sub(month[1], text)
  return text
