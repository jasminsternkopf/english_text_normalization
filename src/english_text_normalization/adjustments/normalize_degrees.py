import re
from typing import Iterable, Tuple

from english_text_normalization.adjustments.unit_abbreviations_normalization import \
    POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION

CELSIUS = re.compile(rf"(\d) ?deg\.? ?C\.?({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})")
#CENTIGRADE = re.compile(rf"(\d) ?deg\.? ?Cent({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})")
FAHRENHEIT = re.compile(
  rf"(\d) ?deg\.? ?F(?:ahr?)?\.?({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})")


def normalize_temperatures_celsius(text: str) -> str:
  text = text.replace("°", " deg.")
  text = CELSIUS.sub(r"\1 degrees Celsius\2", text)
  return text


def normalize_temperatures_fahrenheit(text: str) -> str:
  text = text.replace("°", " deg.")
  text = FAHRENHEIT.sub(r"\1 degrees Fahrenheit\2", text)
  return text


def normalize_temperatures_general(text: str) -> str:
  text = normalize_temperatures_celsius(text)
  text = normalize_temperatures_fahrenheit(text)
  return text

# latitude and longitude

# (\d{1,3}) ?deg\.[^r][^CFota]
# \d' ?.{0,10}(N|E|W|S)\.

# SECONDS = re.compile(r"(\d{1,3} ?deg\.? \d{1,3}(-1/2)?' \d)\"")
# MINUTES = re.compile(r" (\d{1,3} ?deg\.? \d{1,3}(-1/2)?)'")
# DEGREES = re.compile(r"(\d{1,3}) ?deg\.?")

# def normalize_coordinates_in_in_the_footprints_of_the_padres(text: str) -> str:
#   text = SECONDS.sub(r"\1 seconds", text)
#   text = MINUTES.sub(r" \1 minutes", text)
#   text = DEGREES.sub(r"\1 degrees", text)
#   return text


NUMBER_AND_MAYBE_A_HALF = r"\d+(?:-?1/2)?"

# MINUTES_AND_SECONDS = re.compile(rf"({NUMBER_AND_MAYBE_A_HALF})' ?({NUMBER_AND_MAYBE_A_HALF})\"")
# DEGREES_AND_MINUTES = re.compile(rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.? ?({NUMBER_AND_MAYBE_A_HALF})'")
# DEGREES_AND_SECONDS = re.compile(rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.? ?({NUMBER_AND_MAYBE_A_HALF})\"")
# ONLY_DEGREES = re.compile(rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.")

# MINUTES_AND_SECONDS = (re.compile(
#   rf"({NUMBER_AND_MAYBE_A_HALF})' ?({NUMBER_AND_MAYBE_A_HALF})\""), r"\1 minutes \2 seconds")
# DEGREES_AND_MINUTES = (re.compile(
#   rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.? ?({NUMBER_AND_MAYBE_A_HALF})'"), r"\1 degrees \2 minutes")
# DEGREES_AND_SECONDS = (re.compile(
#   rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.? ?({NUMBER_AND_MAYBE_A_HALF})\""), r"\1 degrees \2 seconds")
# ONLY_DEGREES = (re.compile(rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\."), r"\1 degrees")

MINUTES_AND_SECONDS = (
  rf"({NUMBER_AND_MAYBE_A_HALF})',? ?({NUMBER_AND_MAYBE_A_HALF})\"", r"\1 minutes \2 seconds")
DEGREES_AND_MINUTES = (
  rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.?,? ?({NUMBER_AND_MAYBE_A_HALF})'", r"\1 degrees \2 minutes")
DEGREES_AND_SECONDS = (
  rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.?,? ?({NUMBER_AND_MAYBE_A_HALF})\"", r"\1 degrees \2 seconds")
ONLY_DEGREES = (rf"({NUMBER_AND_MAYBE_A_HALF}) ?deg\.", r"\1 degrees")

DMS = [MINUTES_AND_SECONDS, DEGREES_AND_SECONDS, DEGREES_AND_MINUTES, ONLY_DEGREES]

DIRECTION = [(r" N\.", " North"), (r" E\.", " East"),
             (r" S\.", " South"), (r" W\.", " West"), (r"", "")]

DEG_MIN_SEC_WITH_DIRECTIONS = [(re.compile(from_dms + from_dir), to_dms + to_dir)
                               for from_dms, to_dms in DMS for from_dir, to_dir in DIRECTION]


def normalize_degrees_minutes_and_seconds(text: str) -> str:
  text = text.replace("°", " deg.")
  for dms_dir in DEG_MIN_SEC_WITH_DIRECTIONS:
    text = dms_dir[0].sub(dms_dir[1], text)
  return text


LATITUDE = [(r" N\.? lat\.", " North latitude"), (r" S\.? lat\.",
                                                 " South latitude"), (r" lat\.", " latitude")]
LONGITUDE = [(r" W\.? long\.", " West longitude"), (r" E\.? long\.",
                                                   " East longitude"), (r" long\.", " longitude")]


def first_element_of_tuple_to_regex_with_ignore_case(tuple_iter: Iterable[Tuple[str, str]]):
  res = [(re.compile(first_ele, re.IGNORECASE), second_ele) for first_ele, second_ele in tuple_iter]
  return res


LATITUDE_REG = first_element_of_tuple_to_regex_with_ignore_case(LATITUDE)
LONGITUDE_REG = first_element_of_tuple_to_regex_with_ignore_case(LONGITUDE)


def normalize_latitude_and_longitude(text: str) -> str:
  for lat_or_long in [LATITUDE_REG, LONGITUDE_REG]:
    for ele in lat_or_long:
      text = ele[0].sub(ele[1], text)
  return text
