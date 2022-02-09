from english_text_normalization.adjustments.emails import (normalize_emails_and_at,
                                                           replace_at_symbols,
                                                           replace_mail_addresses)


def test_replace_mail_addresses():
  text = "jasmin_sternkopf@web.de is my mail address."
  res = replace_mail_addresses(text)

  assert res == "jasmin_sternkopf at web dot de is my mail address."


def test_replace_at_symbols():
  text = "We slept @ his house."
  res = replace_at_symbols(text)

  assert res == "We slept at his house."
