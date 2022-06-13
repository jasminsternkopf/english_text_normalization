from english_text_normalization.adjustments.remove_dots_that_are_not_end_of_sentence import (
  remove_dot_after_single_capital_letters, remove_dot_after_single_small_letters,
  remove_dot_after_word_not_followed_by_new_sentence, remove_dot_between_word_and_number)

# region remove_dot_after_single_capital_letters


def test_remove_dot_after_single_capital_letters():
  text = "Mrs. L.A.C. Clapp."
  res = remove_dot_after_single_capital_letters(text)

  assert res == "Mrs. L A C Clapp."


def test_remove_dot_after_single_capital_letters__do_not_remove():
  text = "JAN. WASHINGTON'S BIRTHDAY. MARCUS AURELIUS."
  res = remove_dot_after_single_capital_letters(text)

  assert res == text


def test_remove_dot_after_single_capital_letters__with_double_hyphen():
  text = "\"N.B.--Front seats reserved for ladies!\""
  res = remove_dot_after_single_capital_letters(text)

  assert res == "\"N B--Front seats reserved for ladies!\""

# endregion

# region remove_dot_after_single_small_letters


def test_remove_dot_after_single_small_letters():
  text = "See c. five."
  res = remove_dot_after_single_small_letters(text)

  assert res == "See c five."


def test_remove_dot_after_single_small_letters__end_of_sentence__do_not_change():
  text = "I choose option a. What about you?"
  res = remove_dot_after_single_small_letters(text)

  assert res == text

# endregion

# region remove_dot_between_word_and_number


def test_remove_dot_between_word_and_number():
  text = "See cap. 5, s. 4."
  res = remove_dot_between_word_and_number(text)

  assert res == "See cap 5, s 4."

# endregion

# region remove_dot_after_word_not_followed_by_new_sentence


def test_remove_dot_after_word_not_followed_by_new_sentence():
  text = "It was called Number Five, or ad. lib., and consisted of either eggs, fish, a chop, beef-tea, or arrowroot, or anything else of the same value."
  res = remove_dot_after_word_not_followed_by_new_sentence(text)

  assert res == "It was called Number Five, or ad lib, and consisted of either eggs, fish, a chop, beef-tea, or arrowroot, or anything else of the same value."


def test_remove_dot_after_word_not_followed_by_new_sentence__do_not_remove_dot_as_it_is_followed_by_new_sentence():
  text = "Hello World. Hey there!"
  res = remove_dot_after_word_not_followed_by_new_sentence(text)

  assert res == text


def test_remove_dot_after_word_not_followed_by_new_sentence__do_not_remove_dot_as_it_is_followed_by_new_sentence_which_is_a_quote():
  text = "Hello World. \"Hey there!\""
  res = remove_dot_after_word_not_followed_by_new_sentence(text)

  assert res == text


def test_remove_dot_after_word_not_followed_by_new_sentence__do_not_remove():
  text = ""

# endregion
