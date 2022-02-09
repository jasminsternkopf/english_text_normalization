import re

"""
Space, Komma, Punkt klar,
Klammer zu und Semikolon kommen vor,
' und " werden als Maßeinheiten (Inch?) genutzt,
ebenso lb, inch und s (seconds),
% kommt vor

Nicht dabei sein darf/Sonderbehandlung bedarf d (abgedeckt durch pence, zumindest für 2 (todo für 4), vorher behandeln) und th (getrennt behandeln)
"""

CHARS_ALLOWED_AFTER_FRACTION = r"[ ,\.\-);'\":lis%]"

ONE_HALF = re.compile(rf"1/2({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_ONE_IN_NUMERATOR = re.compile(rf"1/(\d+)({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_DENOMINATOR_EQUALS_TWO = re.compile(rf"(\d)/2({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_DENOMINATOR_EQUALS_THREE = re.compile(rf"(\d)/3({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_NUMERATOR_NOT_ONE = re.compile(rf"(\d)/(\d+)({CHARS_ALLOWED_AFTER_FRACTION})")


def normalize_fractions(text: str) -> str:
  text = ONE_HALF.sub(r"one half\1", text)
  #text = text.replace("1/2 ", "one half ")
  text = text.replace("1/3 ", "one third ")
  text = FRACTION_WITH_ONE_IN_NUMERATOR.sub(r"one \1th\2", text)
  text = FRACTION_WITH_DENOMINATOR_EQUALS_TWO.sub(r"\1 halves\2", text)
  text = FRACTION_WITH_DENOMINATOR_EQUALS_THREE.sub(r"\1 thirds\2", text)
  return text
