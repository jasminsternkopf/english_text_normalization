from english_text_normalization.adjustments.write_out_special_characters import (
  normalize_double_quotation_marks, normalize_point_before_numbers,
  normalize_single_quotation_marks_and_apostrophes, replace_hyphen_between_numbers_with_to)

# region normalize_double_quotation_marks


def test_normalize_double_quotation_marks():
  text = "“The Royal Diversion.”"
  res = normalize_double_quotation_marks(text)

  assert res == "\"The Royal Diversion.\""


# endregion

# region normalize_single_quotation_marks_and_apostrophes


def test_normalize_single_quotation_marks_and_apostrophes():
  text = "‘poor little chuck!’"
  res = normalize_single_quotation_marks_and_apostrophes(text)

  assert res == "\"poor little chuck!\""


def test_normalize_single_quotation_marks_and_apostrophes__apostrophes_not_quotation_marks():
  text = "William III.’s reign"
  res = normalize_single_quotation_marks_and_apostrophes(text)

  assert res == "William III.'s reign"

# endregion

# region normalize_point_before_numbers


def test_normalize_point_before_numbers():
  text = "and carbo-hydrates 66·5 per cent"
  res = normalize_point_before_numbers(text)

  assert res == "and carbo-hydrates 66 point 5 per cent"

# endregion

# region replace_hyphen_between_numbers_with_to

def test_replace_hyphen_between_numbers_with_to():
  text = "38-41"
  res = replace_hyphen_between_numbers_with_to(text)

  assert res == "38 to 41"

# endregion

