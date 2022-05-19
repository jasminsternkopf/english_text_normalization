from english_text_normalization.adjustments.other import *


def test_component_quote():
  lines = (
    "\"a\"bc\"",
    "",
    "",
    "'\"abc''",
    "''",
    "\"'\"",
    "\'",
    "\"",
    "\"'`「」『a』〝〟″‹›′“”"
  )
  lines = "\n".join(lines)

  result = remove_quote_start_and_end(lines)

  assert result.splitlines() == [
    "a\"bc",
    "",
    "",
    "abc",
    "",
    "",
    "",
    "",
    "a",
  ]


def test_component_parenthesis():
  lines = (
    "(a(bc)",
    "",
    "",
    "[{abc]]}",
    "((",
    "{}}",
    "[]",
    "()",
    "(){}a[]⟨⟩"
  )
  lines = "\n".join(lines)

  result = remove_parenthesis_start_and_end(lines)

  assert result.splitlines() == [
    "a(bc",
    "",
    "",
    "abc",
    "",
    "",
    "",
    "",
    "a",
  ]
