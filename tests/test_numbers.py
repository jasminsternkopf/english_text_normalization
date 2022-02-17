import re

from english_text_normalization.adjustments.numbers import (
    __expand_number, __number_re, __replace_e_to_the_power_of, __replace_minus,
    expand_and_a_half, normalize_numbers,
    number_to_word_when_number_at_beginning_of_sentence)


def test_replace_e_to_the_power_of__e_minus():
  res = __replace_e_to_the_power_of("e-5654")
  assert res == "ten to the power of minus 5654"


def test_replace_e_to_the_power_of__e_no_minus():
  res = __replace_e_to_the_power_of("e5654")
  assert res == "ten to the power of 5654"


def test_replace_e_to_the_power_of__prefix_e_no_minus():
  res = __replace_e_to_the_power_of("45e5654")
  assert res == "45 times ten to the power of 5654"


def test_replace_e_to_the_power_of__prefix_e_minus():
  res = __replace_e_to_the_power_of("45e-5654")
  assert res == "45 times ten to the power of minus 5654"


def test_replace_minus__normal():
  res = __replace_minus("-5654")
  assert res == "minus 5654"


def test_replace_minus__with_e__no_replacement():
  res = __replace_minus("e-5654")
  assert res == "e-5654"


def test_replace_minus__on_begin__replacement():
  res = __replace_minus("-5654")
  assert res == "minus 5654"


def test_replace_minus__with_space__replacement():
  res = __replace_minus(" -5654")
  assert res == " minus 5654"


def test_normalize_numbers():
  res = normalize_numbers("$5654 -54 5e-21 test $300,000.40")
  assert res == "five thousand, six hundred fifty-four dollars minus fifty-four five times ten to the power of minus twenty-one test three hundred thousand dollars, forty cents"


def test_normalize_numbers__number_contains_comma():
  text = "123,456"
  res = normalize_numbers(text)
  assert res == "one hundred twenty-three thousand, four hundred fifty-six"


def test_normalize_numbers__number_six_digits_without_comma():
  text = "123456"
  res = normalize_numbers(text)
  assert res == "one hundred twenty-three thousand, four hundred fifty-six"


def test_expand_number__number_is_smaller_than_1000():
  m = re.match(__number_re, "999")
  res = __expand_number(m)
  assert res == "nine hundred ninety-nine"


def test_expand_number__number_is_greater_than_3000():
  m = re.match(__number_re, "3001")
  res = __expand_number(m)
  assert res == "three thousand one"


def test_expand_number__number_is_2000():
  m = re.match(__number_re, "2000")
  res = __expand_number(m)
  assert res == "two thousand"


def test_expand_number__number_is_between_2000_and_2010():
  m = re.match(__number_re, "2008")
  res = __expand_number(m)
  assert res == "two thousand eight"


def test_expand_number__number_is_between_1000_and_3000_and_divisible_by_100():
  m = re.match(__number_re, "1400")
  res = __expand_number(m)
  assert res == "fourteen hundred"


def test_expand_number__number_is_between_1000_and_3000_and_divisible_by_100__2():
  m = re.match(__number_re, "2300")
  res = __expand_number(m)
  assert res == "twenty-three hundred"


def test_expand_number__number_is_between_1000_and_3000_and_not_one_of_other_cases():
  m = re.match(__number_re, "1004")
  res = __expand_number(m)
  assert res == "ten oh four"


def test_expand_number__number_is_between_1000_and_3000_and_not_one_of_other_cases__2():
  m = re.match(__number_re, "1987")
  res = __expand_number(m)
  assert res == "nineteen eighty-seven"


def test_expand_number__number_is_undecillion__return_empty_string():
  m = re.match(__number_re, str(10**36))
  res = __expand_number(m)
  assert res == ""


def test_expand_number__number_greater_than_undecillion__return_empty_string():
  m = re.match(__number_re, str(10**36 + 5))
  res = __expand_number(m)
  assert res == ""


def test_expand_and_a_half():
  text = "11-1/2 per cent"
  res = expand_and_a_half(text)

  assert res == "11 and a half per cent"


def test_number_to_word_when_number_at_beginning_of_sentence():
  text = "I want to say two things. 1. Hello! 2. Goodbye."
  res = number_to_word_when_number_at_beginning_of_sentence(text)

  assert res == "I want to say two things. One. Hello! Two. Goodbye."
