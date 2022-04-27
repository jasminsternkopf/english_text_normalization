from english_text_normalization.auxiliary_methods.roman_numerals import (get_all_roman_numerals_up_to_N,
                                                                         roman_units)


def test_roman_units():
  units = roman_units()

  assert units == ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def test_get_all_roman_numerals_up_to_N():
  N = 14
  res = get_all_roman_numerals_up_to_N(14)

  assert res == ["I", "II", "III", "IV", "V", "VI",
                 "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV"]
