from english_text_normalization.adjustments.month_normalization import write_out_month_abbreviations


def test_write_out_month_abbreviations():
  text = " JAN. Feb. mar."
  res = write_out_month_abbreviations(text)

  assert res == " January February March"


def test_write_out_month_abbreviations__nothing_changes():
  text = " October NOVEMBER december"
  res = write_out_month_abbreviations(text)

  assert res == text


def test_write_out_month_abbreviations__jan_several_times():
  text = " JAN. JAN. JAN."
  res = write_out_month_abbreviations(text)

  assert res == " January January January"
