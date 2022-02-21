from english_text_normalization.adjustments.normalizaton_of_certain_words_and_abbr import (
    change_p_dot_before_number_into_page, normalize_per_cent_dot,
    replace_no_with_number)

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

# region normalize_per_cent_dot


def test_normalize_per_cent_dot():
  text = "Its fibre is three per cent., and carbo-hydrates sixty-six point five per cent. Did you know that?"
  res = normalize_per_cent_dot(text)

  assert res == "Its fibre is three percent, and carbo-hydrates sixty-six point five percent. Did you know that?"


def test_normalize_per_cent_dot__with_quotation_marks():
  text = "\"Its fibre is three per cent. and carbo-hydrates sixty-six point five per cent.\" \"Did you know that?\""
  res = normalize_per_cent_dot(text)

  assert res == "\"Its fibre is three percent and carbo-hydrates sixty-six point five percent.\" \"Did you know that?\""


def test_normalize_per_cent_dot__per_cent_at_end_of_direct_speech_but_not_of_sentence():
  text = "\"I hope that you will not declare above a six per cent. dividend at that directors' meeting; at the most, seven per cent.,\" he said."
  res = normalize_per_cent_dot(text)

  assert res == "\"I hope that you will not declare above a six percent dividend at that directors' meeting; at the most, seven percent,\" he said."


def test_normalize_per_cent_dot__question_mark_after_percent():
  text = "\"...he had again flunked you in physics with fifty-nine and a half per cent.?\" \"And he wouldn't raise the mark to sixty! God forgive him,--I cannot.\""
  res = normalize_per_cent_dot(text)

  assert res == "\"...he had again flunked you in physics with fifty-nine and a half percent?\" \"And he wouldn't raise the mark to sixty! God forgive him,--I cannot.\""


def test_normalize_per_cent_dot__double_hyphen_after_percent():
  text = "I've got two thousand laid out at seven per cent.--haven't I, Clara?"
  res = normalize_per_cent_dot(text)

  assert res == "I've got two thousand laid out at seven percent--haven't I, Clara?"


def test_normalize_per_cent_dot__double_hyphen_after_percent_but_end_of_sentence():
  text = "I've got two thousand laid out at seven per cent.--Haven't I, Clara?"
  res = normalize_per_cent_dot(text)

  assert res == "I've got two thousand laid out at seven percent.--Haven't I, Clara?"

# endregion
