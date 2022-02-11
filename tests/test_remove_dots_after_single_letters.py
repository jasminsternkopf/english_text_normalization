from english_text_normalization.adjustments.remove_dots_after_single_letters import \
    remove_dot_after_single_capital_letters

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
