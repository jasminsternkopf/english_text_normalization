import re

# START_QUOTE_PATTERN = re.compile("(\n?)[\"']+([^\n]*)(\n?)")
QUOTES = "\"'`「」『』〝〟″⟨⟩‹›′“”"
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
