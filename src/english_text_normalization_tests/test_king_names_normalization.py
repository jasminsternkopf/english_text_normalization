from english_text_normalization.adjustments.king_names_normalization import (
  add_the_between_king_name_and_roman_numeral, normalize_king_name_followed_by_roman_numeral,
  normalize_king_names_general)


def test_add_the_between_king_name_and_roman_numeral():
  text = "Charles II, Paul IVth and Henry III."
  res = add_the_between_king_name_and_roman_numeral(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the II, Paul IVth and Henry the III"


def test_add_the_between_king_name_and_roman_numeral__roman_numeral_last_in_str():
  text = "Henry III."
  res = add_the_between_king_name_and_roman_numeral(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Henry the III"


def test_normalize_king_names_general__roman_numeral_last_in_str():
  text = "Henry III.,"
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Henry the third,"


def test_normalize_king_names_general__component_test():
  text = "Charles II, Paul IVth and Henry III. were kings."
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the second, Paul IVth and Henry the third were kings."


def test_normalize_king_names_general__is_III_recognized_as_three_even_without_dot():
  text = "Charles III "
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the third "


def test_normalize_king_names_general__the_was_already_between_name_and_numeral():
  text = "Charles the II."
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the second."


def test_normalize_king_names_general__not_kings_name_followed_by_the_and_numeral():
  text = "I read the IX. book"
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "I read the ninth book"


def test_normalize_king_names_general__second_with_different_versions():
  text = "Charles the IInd, Charles IId Charles IId. Charles IInd. "
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the second, Charles the second Charles the second Charles the second "


def test_normalize_king_names_general__third_with_different_versions():
  text = "Charles the IIId, Charles IIIrd Charles IIIrd. "
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the third, Charles the third Charles the third "


def test_normalize_king_names_general__fourth_with_different_versions():
  text = "Charles the IVth, Charles IVth. Charles IV. "
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Charles"})

  assert res == "Charles the fourth, Charles the fourth Charles the fourth "


def test_normalize_king_names_general__king_name_that_is_not_in_safe_king_names_not_replaced_for_I_V_and_X():
  text = "Charles I., Charles V and Charles X won't be replaced."
  res = normalize_king_names_general(text, {"Charles", "Henry"}, {"Henry"})

  assert res == text


def test_normalize_king_name_followed_by_roman_numeral():
  text = "Sigismund XIX was a king."
  res = normalize_king_name_followed_by_roman_numeral(text)

  assert res == "Sigismund the nineteenth was a king."


def test_normalize_king_name_followed_by_roman_numeral__without_dot():
  text = "Charles III and James I, Henry V, Fred X and Edward VI were kings."
  res = normalize_king_name_followed_by_roman_numeral(text)

  assert res == "Charles the third and James the first, Henry the fifth, Fred the tenth and Edward the sixth were kings."
