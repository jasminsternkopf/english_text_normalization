from english_text_normalization.adjustments.money_normalization import (
    normalize_pence, normalize_pounds, normalize_pounds_shillings_and_pence,
    normalize_shillings, normalize_shillings_and_pounds_with_dots,
    normalize_shillings_and_pounds_without_dots)

# region normalize_pounds


def test_normalize_pounds__number_of_pounds_contains_comma():
  text = " L12,345 2s. 3d."
  res = normalize_pounds(text)

  assert res == " 12,345 pounds 2s. 3d."


def test_normalize_pounds__dot_after_number_of_pounds():
  text = " L12. 2s. 3d."
  res = normalize_pounds(text)

  assert res == " 12 pounds 2s. 3d."


def test_normalize_pounds__only_numbers_directly_after_L():
  text = " L12 2s. 3d."
  res = normalize_pounds(text)

  assert res == " 12 pounds 2s. 3d."


def test_normalize_pounds__dot_after_L__no_shillings_or_pence():
  text = " L.10,875,870 "
  res = normalize_pounds(text)

  assert res == " 10,875,870 pounds "


def test_normalize_pounds__dot_after_L():
  text = " L.499,833, 11s. 6d."
  res = normalize_pounds(text)

  assert res == " 499,833 pounds 11s. 6d."


def test_normalize_pounds__space_after_L():
  text = " L 12,345 2s. 3d."
  res = normalize_pounds(text)

  assert res == " 12,345 pounds 2s. 3d."


def test_normalize_pounds__dot_and_space_after_L():
  text = " L. 12,345 2s. 3d."
  res = normalize_pounds(text)

  assert res == " 12,345 pounds 2s. 3d."


def test_normalize_pounds__one_pound():
  text = " L.1 2s. 3d."
  res = normalize_pounds(text)

  assert res == " one pound 2s. 3d."


def test_normalize_pounds__one_and_comma_after_L_but_is_not_one():
  text = " L.1,000 2s. 3d."
  res = normalize_pounds(text)

  assert res == " 1,000 pounds 2s. 3d."

  # endregion

# region normalize_shillings


def test_normalize_shillings__dot_and_space_after_s():
  text = " 2s. 3d."
  res = normalize_shillings(text)

  assert res == " 2 shillings 3d."


def test_normalize_shillings__dot_and_space_after_number():
  text = " 2 s. 3 d."
  res = normalize_shillings(text)

  assert res == " 2 shillings 3 d."


def test_normalize_shillings__space_after_s():
  text = " 2s 3d."
  res = normalize_shillings(text)

  assert res == " 2 shillings 3d."


def test_normalize_shillings__only_dot_after_s():
  text = " 2s.3d."
  res = normalize_shillings(text)

  assert res == " 2 shillings 3d."


def test_normalize_shillings__number_of_shillings_consists_of_two_digits():
  text = " 12s. 3d."
  res = normalize_shillings(text)

  assert res == " 12 shillings 3d."

# endregion

# region normalize_shillings_and_pounds_without_dots


def test_normalize_shillings_and_pounds_without_dots__space_after_number():
  text = " 2 s 3 d."
  res = normalize_shillings_and_pounds_without_dots(text)

  assert res == " 2 shillings 3 pence."


def test_normalize_shillings_and_pounds_without_dots():
  text = " 2s 3d."
  res = normalize_shillings_and_pounds_without_dots(text)

  assert res == " 2 shillings 3 pence."


def test_normalize_shillings_and_pounds_without_dots__comma_after_shillings():
  text = " 2s, 3d."
  res = normalize_shillings_and_pounds_without_dots(text)

  assert res == " 2 shillings 3 pence."

# endregion

# region normalize_shillings_and_pounds_with_dots


def test_normalize_shillings_and_pounds_with_dots():
  text = " 2s. 3d. "
  res = normalize_shillings_and_pounds_with_dots(text)

  assert res == " 2 shillings 3 pence "


def test_normalize_shillings_and_pounds_with_dots__space_after_number():
  text = " 2 s. 3 d. "
  res = normalize_shillings_and_pounds_with_dots(text)

  assert res == " 2 shillings 3 pence "


def test_normalize_shillings_and_pounds_with_dots__comma_after_shillings():
  text = " 2s., 3d. "
  res = normalize_shillings_and_pounds_with_dots(text)

  assert res == " 2 shillings 3 pence "

# endregion

# region normalize_pence


def test_normalize_pence__one_penny():
  text = " 1d. "
  res = normalize_pence(text)

  assert res == " one penny "


def test_normalize_pence__one_penny__space_after_one():
  text = " 1 d. "
  res = normalize_pence(text)

  assert res == " one penny "


def test_normalize_pence__one_penny__no_dot_after_d():
  text = " 1d "
  res = normalize_pence(text)

  assert res == " one penny "


def test_normalize_pence__word_after_one_do_not_normalize():
  text = " 1 dozen"
  res = normalize_pence(text)

  assert res == text


def test_normalize_pence__word_after_four_do_not_normalize():
  text = " 4 dozen"
  res = normalize_pence(text)

  assert res == text


def test_normalize_pence__and_a_half_pence():
  text = " 11-1/2d "
  res = normalize_pence(text)

  assert res == " 11 and a half pence "


def test_normalize_pence__and_a_half_pence__dot_after_d():
  text = " 11-1/2d. "
  res = normalize_pence(text)

  assert res == " 11 and a half pence "


def test_normalize_pence__and_a_half_pence__no_hyphen_before_half():
  text = " 11/2d "
  res = normalize_pence(text)

  assert res == " 1 and a half pence "


def test_normalize_pence__and_a_half_pence__space_after_half():
  text = " 11-1/2 d "
  res = normalize_pence(text)

  assert res == " 11 and a half pence "


def test_normalize_pence__10_pence():
  text = " 10d. "
  res = normalize_pence(text)

  assert res == " 10 pence "


def test_normalize_pence__4_pence__space_after_number():
  text = " 4 d. "
  res = normalize_pence(text)

  assert res == " 4 pence "


def test_normalize_pence__4_pence__no_dot_after_d():
  text = " 4d "
  res = normalize_pence(text)

  assert res == " 4 pence "


def test_normalize_pence__number_of_pence_consists_of_more_than_one_char():
  text = " 11-1/4d. "
  res = normalize_pence(text)

  assert res == " 11-1/4 pence "

# endregion

# region normalize_pounds_shillings_and_pence


def test_normalize_pounds_shillings_and_pence__all_three():
  text = " L12 2s. 3d. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 12 pounds 2 shillings 3 pence "


def test_normalize_pounds_shillings_and_pence__all_three__with_commata():
  text = " L12, 2s., 3d. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 12 pounds 2 shillings 3 pence "


def test_normalize_pounds_shillings_and_pence__only_pounds():
  text = " L12. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 12 pounds "


def test_normalize_pounds_shillings_and_pence__only_shillings_and_pence_without_dots():
  text = " 2s 3d "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 2 shillings 3 pence "


def test_normalize_pounds_shillings_and_pence__only_shillings_and_pence_without_spaces_but_with_dots():
  text = " 2s.3d. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 2 shillings 3 pence "


def test_normalize_pounds_shillings_and_pence__only_shillings():
  text = " 3s. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 3 shillings "


def test_normalize_pounds_shillings_and_pence__only_pence():
  text = " 6d. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 6 pence "


def test_normalize_pounds_shillings_and_pence__pence_number_contains_a_half():
  text = " L1, 1s., 11/2d. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " one pound one shilling 1 and a half pence "


def test_normalize_pounds_shillings_and_pence__all_three_but_only_pence_non_zero():
  text = " L0. 0s. 3d. "
  res = normalize_pounds_shillings_and_pence(text)

  assert res == " 0 pounds 0 shillings 3 pence "

# endregion
