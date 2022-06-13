from english_text_normalization.adjustments.fraction_normalization import normalize_fractions


def test_normalize_fractions__one_half():
  text = "1/2, "
  res = normalize_fractions(text)

  assert res == "one half, "
