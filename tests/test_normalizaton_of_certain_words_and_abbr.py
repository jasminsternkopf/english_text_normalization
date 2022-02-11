from english_text_normalization.adjustments.normalizaton_of_certain_words_and_abbr import \
    replace_no_with_number

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
