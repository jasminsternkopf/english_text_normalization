import re

QUOTES = r"\"'`「」『』〝〟″‹›′“”"
# Line starting
QUOTE_PATTERN1 = re.compile(rf"\n[{QUOTES}]+")
# Line ending
QUOTE_PATTERN2 = re.compile(rf"[{QUOTES}]+\n")
# Text starting
QUOTE_PATTERN3 = re.compile(rf"^[{QUOTES}]+")
# Text ending
QUOTE_PATTERN4 = re.compile(rf"[{QUOTES}]+$")


def remove_quote_start_and_end(text: str) -> str:
  text = QUOTE_PATTERN1.sub(r"\n", text)
  text = QUOTE_PATTERN2.sub(r"\n", text)
  text = QUOTE_PATTERN3.sub(r"", text)
  text = QUOTE_PATTERN4.sub(r"", text)
  return text


PARENTHESES = r"\(\)\[\]\{\}⟨⟩【】"
# Line starting
PARENTHESIS_PATTERN1 = re.compile(rf"\n[{PARENTHESES}]+")
# Line ending
PARENTHESIS_PATTERN2 = re.compile(rf"[{PARENTHESES}]+\n")
# Text starting
PARENTHESIS_PATTERN3 = re.compile(rf"^[{PARENTHESES}]+")
# Text ending
PARENTHESIS_PATTERN4 = re.compile(rf"[{PARENTHESES}]+$")


def remove_parenthesis_start_and_end(text: str) -> str:
  text = PARENTHESIS_PATTERN1.sub(r"\n", text)
  text = PARENTHESIS_PATTERN2.sub(r"\n", text)
  text = PARENTHESIS_PATTERN3.sub(r"", text)
  text = PARENTHESIS_PATTERN4.sub(r"", text)
  return text


SENTENCE_PUNCTUATION = r"\.\?\!;:,"
SENTENCE_PUNCTUATION_PATTERN = re.compile(rf"\s+([{SENTENCE_PUNCTUATION}])")


def remove_whitespace_before_sentence_punctuation(text: str) -> str:
  text = SENTENCE_PUNCTUATION_PATTERN.sub(r"\1", text)
  return text
