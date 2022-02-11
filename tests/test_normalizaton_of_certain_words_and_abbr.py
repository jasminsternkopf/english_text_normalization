from english_text_normalization.adjustments.normalizaton_of_certain_words_and_abbr import (
    change_p_dot_before_number_into_page, replace_no_with_number)

# region replace_no_with_number


def test_replace_no_with_number():
  text = "No. 1, Newgate Street"
  res = replace_no_with_number(text)

  assert res == "number 1, Newgate Street"


def test_replace_no_with_number__no_starting_with_small_letter():
  text = "I said no. "
  res = replace_no_with_number(text)

  assert res == text

# endregion

# region change_p_dot_before_number_into_page


def test_change_p_dot_before_number_into_page__singular():
  text = "See p. 44."
  res = change_p_dot_before_number_into_page(text)

  assert res == "See page 44."


def test_change_p_dot_before_number_into_page__plural_with_hyphen():
  text = "See p. 44-46."
  res = change_p_dot_before_number_into_page(text)

  assert res == "See pages 44-46."


def test_change_p_dot_before_number_into_page__plural_with_comma():
  text = "See p. 44, 46."
  res = change_p_dot_before_number_into_page(text)

  assert res == "See pages 44, 46."

# endregion
