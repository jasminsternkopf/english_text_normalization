import re


def replace_no_with_number(text: str) -> str:
  text = text.replace("No. ", "number ")
  return text


def replace_nos_with_numbers(text: str) -> str:
  text = text.replace("Nos. ", "numbers ")
  return text


def normalize_today_and_tomorrow(text: str) -> str:
  text = text.replace("To-day", "Today")
  text = text.replace("to-day", "today")
  text = text.replace("To-morrow", "Tomorrow")
  text = text.replace("to-morrow", "tomorrow")
  return text


# GEO_AND_C_OR_CAP = re.compile(r"Geo\. ([IVX]{1,3}\.) (c(ap)?)\. (\d)")
# S_AFTER_GEO = re.compile(r", s. (\d)")
# GEO = re.compile(r"Geo\. ([IVX]{1,3}\.)")


# def geo_to_george(text: str) -> str:  # brauch ich das?
#   #text = text.replace("Geo.", "George")
#   text = GEO_AND_C_OR_CAP.sub(r"George \1 \2 \4", text)
#   text = S_AFTER_GEO.sub(r", s \1", text)
#   text = GEO.sub(r"George \1", text)
#   return text


def remove_sic(text: str) -> str:
  text = text.replace(" [sic]", "")
  return text


IE_SMALL = re.compile(r" i\. ?e\.")
IE_CAPITAL_I = re.compile(r" I\. ?e\.")


def replace_ie_with_that_is(text: str) -> str:
  text = IE_SMALL.sub(" that is", text)
  text = IE_CAPITAL_I.sub(" That is", text)
  return text


EG_SMALL = re.compile(r" e\. ?g\.")
EG_CAPITAL_E = re.compile(r" E\. ?g\.")


def replace_eg_with_for_example(text: str) -> str:
  text = EG_SMALL.sub(" for example", text)
  text = EG_CAPITAL_E.sub(" For example", text)
  return text


def replace_etc_with_et_cetera(text: str) -> str:
  text = text.replace("etc.", "et cetera")
  text = text.replace("Etc.", "Et cetera")
  return text


VG_SMALL = re.compile(r" v\. ?g\.")
VG_CAPITAL_V = re.compile(r" V\. ?g\.")


def replace_vg_with_for_instance(text: str) -> str:
  text = VG_SMALL.sub(" for instance", text)
  text = VG_CAPITAL_V.sub(" For instance", text)
  return text


def geo_to_george(text: str) -> str:
  text = text.replace(" Geo. ", " George ")
  return text


P_DOT_BEFORE_RANGE_OF_NUMBERS = re.compile(r" p\. (\d+-\d+)")
P_DOT_BEFORE_NUMBERS_SEPARATED_BY_COMMA = re.compile(r" p\. (\d+, \d+\b)")
P_DOT_BEFORE_NUMBER = re.compile(r" p\. (\d)")
# pp. auch TODO


def change_p_dot_before_number_into_page(text: str) -> str:
  text = P_DOT_BEFORE_RANGE_OF_NUMBERS.sub(r" pages \1", text)
  text = P_DOT_BEFORE_NUMBERS_SEPARATED_BY_COMMA.sub(r" pages \1", text)
  text = P_DOT_BEFORE_NUMBER.sub(r" page \1", text)
  return text


#  [a-hj-oq-uw-z]\. [^A-Z]
