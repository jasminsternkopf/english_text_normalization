import re
from typing import List, Pattern, Tuple

MONTH_MAPPINGS: List[Tuple[Pattern, str]] = [
  (re.compile(" jan\.", re.IGNORECASE), " January"),
  (re.compile(" feb\.", re.IGNORECASE), " February"),
  (re.compile(" mar\.", re.IGNORECASE), " March"),
  (re.compile(" apr\.", re.IGNORECASE), " April"),
  (re.compile(" aug\.", re.IGNORECASE), " August"),
  (re.compile(" sept\.", re.IGNORECASE), " September"),
  (re.compile(" oct\.", re.IGNORECASE), " October"),
  (re.compile(" nov\.", re.IGNORECASE), " November"),
  (re.compile(" dec\.", re.IGNORECASE), " December")
]


def write_out_month_abbreviations(text: str) -> str:
  for month in MONTH_MAPPINGS:
    text = month[0].sub(month[1], text)
  return text
