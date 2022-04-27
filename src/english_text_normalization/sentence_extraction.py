import re

SENTENCE_ENDS = [".", "?", "!"]
SENTENCE_ENDS = [re.escape(x) for x in SENTENCE_ENDS]
#SENTENCE_ENDS_AND_CAPITAL_LETTER = [re.compile(rf"({end}\"?)(?: |\-\-|\.\.\.)(\"?[A-Z])") for end in SENTENCE_ENDS]
#SENTENCE_ENDS_AND_CAPITAL_LETTER = [re.compile(rf"({end}\"?'?\)?) (?:-- )?(\(?'?\"?[A-Z])") for end in SENTENCE_ENDS]
#
# SENTENCE_ENDS_AND_CAPITAL_LETTER = [re.compile(
#  rf"({end}\"?\)?) (?:-- )?(\(?\"?[A-Z])") for end in SENTENCE_ENDS]
SENTENCE_ENDS_AND_CAPITAL_LETTER = [re.compile(
  rf"({end}[\"')]{{0,3}}) (?:-- )?([\"'(]{{0,3}}[A-Z])") for end in SENTENCE_ENDS]


def extract_sentences(text: str) -> str:
  for sentence_end in SENTENCE_ENDS_AND_CAPITAL_LETTER:
    text = sentence_end.sub(r"\1\n\2", text)
  text = remove_quotation_marks_in_line_if_uneven_number_of_them(text)
  # text = remove_quotation_marks_in_line_if_uneven_number_of_them( text, "'")  # TODO entfernt ' bei 's, nicht so clever
  return text


def remove_quotation_marks_in_line_if_uneven_number_of_them(text: str, quotation_mark: str = "\"") -> str:
  sentences = text.split("\n")
  new_sentences = []
  for sentence in sentences:
    if sentence.count(quotation_mark) % 2 == 1:
      sentence = sentence.replace(quotation_mark, "")
    new_sentences.append(sentence)
  new_sentences_single_string = "\n".join(new_sentences)
  return new_sentences_single_string
