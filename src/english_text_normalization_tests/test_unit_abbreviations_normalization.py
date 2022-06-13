import re

from english_text_normalization.adjustments.unit_abbreviations_normalization import (
  UNIT_MAPPINGS_TIME_SINGULAR, get_plural_abbreviations, get_unit_abbreviations_as_regex,
  normalize_all_units, normalize_given_units, normalize_length_units, normalize_time_units,
  normalize_weight_units)

# region get_plural_abbreviations


def test_get_plural_abbreviations():
  abbr_from_to = UNIT_MAPPINGS_TIME_SINGULAR
  res = get_plural_abbreviations(abbr_from_to)

  assert res == [('sec', 'seconds'), ('s', 'seconds'), ('min', 'minutes')]

# endregion

# region get_unit_abbreviations_as_regex


def xtest_get_unit_abbreviations_as_regex():
  abbr_from_to = [("min", "minute")]
  res_1, res_2 = get_unit_abbreviations_as_regex(abbr_from_to)

  assert res_1 == [(re.compile(" 1 ?min\\.?([ ,:;)\'\\\"\\.!\\?])"), " 1 minute\\1")]
  #assert res_1 == [(re.compile(' 1 ?min\\.?([ ,:;)\'\\"])'), " one minute\\1")]
  assert res_2 == [(re.compile("(\\d) ?mins?\\.?([ ,:;)\'\\\"\\.!\\?])"), "\\1 minutes\\2")]


def xtest_get_unit_abbreviations_as_regex__no_dot_after_abbr():
  abbr_from_to = [("min", "minute")]
  res_1, res_2 = get_unit_abbreviations_as_regex(abbr_from_to, dot="never")

  assert res_1 == [(re.compile(" 1 ?min([ ,:;)\'\\\"\\.!\\?])"), " 1 minute\\1")]
  assert res_2 == [(re.compile("(\\d) ?mins?([ ,:;)\'\\\"\\.!\\?])"), "\\1 minutes\\2")]

# endregion

# region normalize_given_units


def test_normalize_abbreviated_units():
  text = "He needed 5mins 1s to get there."
  res = normalize_given_units(text, UNIT_MAPPINGS_TIME_SINGULAR)

  assert res == "He needed 5 minutes 1 second to get there."


def test_normalize_abbreviated_units__only_normalizes_when_dot_after_abbreviation():
  text = "He needed 5mins 1s to get there."
  res = normalize_given_units(text, UNIT_MAPPINGS_TIME_SINGULAR, dot="always")

  assert res == text

# endregion

# region normalize_time_units


def test_normalize_time_units():
  text = "He ran the marathon in 1h. 3m 2sec, while she needed 6h 12 m. 1s!"
  res = normalize_time_units(text)

  assert res == "He ran the marathon in 1 hour 3 minutes 2 seconds, while she needed 6 hours 12 minutes 1 second!"


# endregion

# region normalize_length_units


def test_normalize_length_units():
  text = "I can tell you: 1 in. is approximately the same as 2.54cm."
  res = normalize_length_units(text)

  assert res == "I can tell you: 1 inch is approximately the same as 2.54 centimeters."


def test_normalize_length_units__US():
  text = "3 ft is longer than 2ft. which is longer than 1ft."
  res = normalize_length_units(text, system="US")

  assert res == "3 feet is longer than 2 feet which is longer than 1 foot."

# endregion

# region normalize_weight_units


def test_normalize_weight_units():
  text = "I can tell you: 1 kg is approximately the same as 2lb."
  res = normalize_weight_units(text)

  assert res == "I can tell you: 1 kilogram is approximately the same as 2 pounds."


def test_normalize_weight_units__2():
  text = "I can tell you: 1 kg is approximately the same as 2lb. But not exactly."
  res = normalize_weight_units(text)

  assert res == "I can tell you: 1 kilogram is approximately the same as 2 pounds But not exactly."

# endregion

# region normalize_all_units


def test_normalize_all_units():
  text = "One ft., 1 in, 2kg; 3 mi and 1sec are units."
  res = normalize_all_units(text)

  assert res == "One ft., 1 in, 2 kilograms; 3 miles and 1 second are units."

# endregion
