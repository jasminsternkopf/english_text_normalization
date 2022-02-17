import re

# _mappings = [
#   ('mrs', 'misess'),
#   ('mr', 'mister'),
#   ('dr', 'doctor'),
#   ('st', 'saint'),
#   ('co', 'company'),
#   ('jr', 'junior'),
#   ('maj', 'major'),
#   ('gen', 'general'),
#   ('drs', 'doctors'),
#   ('rev', 'reverend'),
#   ('lt', 'lieutenant'),
#   ('hon', 'honorable'),
#   ('sgt', 'sergeant'),
#   ('capt', 'captain'),
#   ('esq', 'esquire'),
#   ('ltd', 'limited'),
#   ('col', 'colonel'),
#   ('ft', 'fort'),
# ]

_mappings = [
  ('Mrs', 'Misess'),
  ('Mr', 'Mister'),
  ('Dr', 'Doctor'),
  ('St', 'Saint'),
  ('Sta', 'Santa'),  # kommt nur bei Lectures on Painting vor
  ('Co', 'Company'),
  ('Jr', 'Junior'),
  ('Maj', 'Major'),
  ('Gen', 'General'),  # kommt glaube nicht vor
  ('Drs', 'Doctors'),
  ('Rev', 'Reverend'),
  ('Lt', 'Lieutenant'),  # kommt glaube nicht vor
  ('Lieut', 'Lieutenant'),
  ('Hon', 'Honorable'),
  ('Sgt', 'Sergeant'),  # kommt glaube nicht vor
  ('Capt', 'Captain'),  # kommt glaube nicht vor
  ('Esq', 'Esquire'),
  ('ltd', 'limited'),  # kommt glaube nicht vor, keine Ahnung ob groß oder klein
  ('Col', 'Colonel'),  # kommt glaube nicht vor
  ('ft', 'fort'),  # kommt glaube nicht vor, keine Ahnung ob groß oder klein
  ('MM', 'Messieurs'),
  ('Bart', 'Baronet')
]

# List of (regular expression, replacement) pairs for abbreviations:
#_abbreviations = [(re.compile(rf'\b{fr}\.', re.IGNORECASE), to) for fr, to in _mappings]
_abbreviations = [(re.compile(rf'\b{fr}\.'), to) for fr, to in _mappings]


def expand_abbreviations(text: str) -> str:
  for regex, replacement in _abbreviations:
    text = re.sub(regex, replacement, text)
  return text


_unit_mappings = [
  ('g', 'grams'),
  ('kg', 'kilograms'),
  ('mm', 'millimeters'),
  ('cm', 'centimeters'),
  ('m', 'meters'),
  ('sec', 'seconds'),
  ('s', 'seconds'),
  ('min', 'minutes'),
]

_unit_abbreviations = [(re.compile(rf"\s{fr}\b"), f" {to}") for fr, to in _unit_mappings]


def expand_units_of_measure(text: str) -> str:
  # TODO: here case for singular: 1 cm -> centimeter
  for regex, replacement in _unit_abbreviations:
    text = re.sub(regex, replacement, text)
  return text


_big_letter_re = re.compile(r'([A-Z])([A-Z])')


def replace_big_letter_abbreviations(text: str) -> str:
  while len(re.findall(_big_letter_re, text)) > 0:
    text = re.sub(_big_letter_re, r'\1 \2', text)
  return text
