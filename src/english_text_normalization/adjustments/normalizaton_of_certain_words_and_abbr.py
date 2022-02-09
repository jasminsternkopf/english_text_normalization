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


GEO_AND_C_OR_CAP = re.compile(r"Geo\. ([IVX]{1,3}\.) (c(ap)?)\. (\d)")
S_AFTER_GEO = re.compile(r", s. (\d)")
GEO = re.compile(r"Geo\. ([IVX]{1,3}\.)")


def geo_to_george(text: str) -> str:  # brauch ich das?
  #text = text.replace("Geo.", "George")
  text = GEO_AND_C_OR_CAP.sub(r"George \1 \2 \4", text)
  text = S_AFTER_GEO.sub(r", s \1", text)
  text = GEO.sub(r"George \1", text)
  return text


def remove_sic(text: str) -> str:
  text = text.replace(" [sic]", "")
  return text


# def expand_latin_abbreviations(text: str) -> str:
#   text = text.replace("e.g.", "for example")
#   text = text.replace("etc.", "et cetera")
#   return text

def replace_ie_with_that_is(text: str) -> str:
  text = text.replace("i.e.", "that is")
  text = text.replace("I.e.", "That is")
  return text


def replace_eg_with_for_example(text: str) -> str:
  text = text.replace("e.g.", "for example")
  text = text.replace("E.g.", "For example")
  return text


def replace_etc_with_et_cetera(text: str) -> str:
  text = text.replace("etc.", "et cetera")
  text = text.replace("Etc.", "Et cetera")
  return text


def geo_to_george_general(text: str) -> str:
  text = text.replace(" Geo. ", " George ")
  return text
