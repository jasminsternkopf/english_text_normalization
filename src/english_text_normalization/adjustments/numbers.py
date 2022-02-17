import re
from logging import getLogger
from typing import Match

import inflect

UNDECILLION = 10**36

__inflect = inflect.engine()
__comma_number_re = re.compile(r'([0-9][0-9\,]+[0-9])')
__decimal_number_re = re.compile(r'([0-9]+\.[0-9]+)')
__pounds_re = re.compile(r'£([0-9\,]*[0-9]+)')
__dollars_re = re.compile(r'\$([0-9\.\,]*[0-9]+)')
__ordinal_re = re.compile(r'[0-9]+(st|nd|rd|th)')
__number_re = re.compile(r'[0-9]+')

__e_re = re.compile(r'\be([0-9]+)')
__e_minus_re = re.compile(r'\be-([0-9]+)')
__factor_e_re = re.compile(r'([0-9]+)e([0-9]+)')
__factor_e_minus_re = re.compile(r'([0-9]+)e-([0-9]+)')

__minus_re = re.compile(r'(\s|^)-([0-9]+)')


def __remove_commas(m: Match) -> str:
  return m.group(1).replace(',', '')


def __expand_decimal_point(m: Match) -> str:
  return m.group(1).replace('.', ' point ')


def __expand_dollars(m: Match) -> str:
  match = m.group(1)
  parts = match.split('.')
  if len(parts) > 2:
    return match + ' dollars'  # Unexpected format
  dollars = int(parts[0]) if parts[0] else 0
  cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0
  if dollars and cents:
    dollar_unit = 'dollar' if dollars == 1 else 'dollars'
    cent_unit = 'cent' if cents == 1 else 'cents'
    return '%s %s, %s %s' % (dollars, dollar_unit, cents, cent_unit)
  elif dollars:
    dollar_unit = 'dollar' if dollars == 1 else 'dollars'
    return '%s %s' % (dollars, dollar_unit)
  elif cents:
    cent_unit = 'cent' if cents == 1 else 'cents'
    return '%s %s' % (cents, cent_unit)
  else:
    return 'zero dollars'


def __expand_ordinal(m: Match) -> str:
  return __inflect.number_to_words(m.group(0))


def __expand_number(m: Match) -> str:
  num = int(m.group(0))
  if num >= UNDECILLION:
    # Inflect does not support this until now.
    logger = getLogger(__name__)
    logger.warning(
      f"Failed normalizing number: \"{m.string}\". Therefore replaced it with nothing.")
    return ""
  if num <= 1000 or 2000 <= num < 2010 or num >= 3000:
    return __inflect.number_to_words(num, andword='')
  if num % 100 == 0:
    return __inflect.number_to_words(num // 100) + ' hundred'
  return __inflect.number_to_words(num, andword='', zero='oh', group=2).replace(', ', ' ')


def __replace_e_to_the_power_of(text: str) -> str:
  text = re.sub(__e_minus_re, r'ten to the power of minus \1', text)
  text = re.sub(__e_re, r'ten to the power of \1', text)
  text = re.sub(__factor_e_minus_re, r'\1 times ten to the power of minus \2', text)
  text = re.sub(__factor_e_re, r'\1 times ten to the power of \2', text)
  return text


def __replace_minus(text: str) -> str:
  text = re.sub(__minus_re, r'\1minus \2', text)
  return text


def normalize_numbers(text: str) -> str:
  text = __replace_e_to_the_power_of(text)
  text = __replace_minus(text)
  text = re.sub(__comma_number_re, __remove_commas, text)
  text = re.sub(__pounds_re, r'\1 pounds', text)
  text = re.sub(__dollars_re, __expand_dollars, text)
  text = re.sub(__decimal_number_re, __expand_decimal_point, text)
  text = re.sub(__ordinal_re, __expand_ordinal, text)
  text = re.sub(__number_re, __expand_number, text)
  return text


def expand_and_a_half(text: str) -> str:
  text = text.replace("-1/2", " and a half")
  return text


def normalize_second_and_third_when_abbr_with_d(text: str) -> str:
  # TODO
  text = text.replace("22d", "twenty-second")
  text = text.replace("2d", "second")
  text = text.replace("3d", "third")
  return text


SENTENCE_ENDS = [".", "?", "!"]
SENTENCE_ENDS = [re.escape(x) for x in SENTENCE_ENDS]
NUMBER_AT_BEGINNING_OF_SENTENCE = [re.compile(
  rf"{end}[\"')]{{0,3}} +(?:-- )?\"?\d+") for end in SENTENCE_ENDS]

NUMBER = re.compile(r"\d+")


def replace_match(match) -> str:
  text = match.group()
  number = NUMBER.search(text)
  number_as_word_with_first_capital_letter = normalize_numbers(number.group()).capitalize()
  replacement = NUMBER.sub(number_as_word_with_first_capital_letter, text)
  return replacement


def number_to_word_when_number_at_beginning_of_sentence(text: str) -> str:
  for number_at_beginning_of_sentence in NUMBER_AT_BEGINNING_OF_SENTENCE:
    text = number_at_beginning_of_sentence.sub(replace_match, text)
  return text
