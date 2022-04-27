from english_text_normalization.sentence_extraction import (
    extract_sentences, remove_quotation_marks_in_line_if_uneven_number_of_them)


def normalizer(text: str) -> str:
  return text


def test_extract_sentences__dot():
  text = "Hello World. It's a pleasure."
  res = extract_sentences(text, normalizer)

  assert res == "Hello World.\nIt's a pleasure."


def test_extract_sentences__both_sentences_direct_speech():
  text = "\"Hello World.\" \"It's a pleasure.\""
  res = extract_sentences(text, normalizer)

  assert res == "\"Hello World.\"\n\"It's a pleasure.\""


def test_extract_sentences__both_sentences_direct_speech_with_apostrophes_as_quotation_marks():
  text = "'Hello World.' 'It's a pleasure.'"
  res = extract_sentences(text, normalizer)

  assert res == "'Hello World.'\n'It's a pleasure.'"


def test_extract_sentences__exclamation_mark():
  text = "Hello World! It's a pleasure."
  res = extract_sentences(text, normalizer)

  assert res == "Hello World!\nIt's a pleasure."


def test_extract_sentences__question_mark():
  text = "Hello World? It's a pleasure."
  res = extract_sentences(text, normalizer)

  assert res == "Hello World?\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_dot():
  text = "\"Hello World.\" she said. It's a pleasure."
  res = extract_sentences(text, normalizer)

  assert res == "\"Hello World.\" she said.\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_exclamation_mark():
  text = "\"Hello World!\" she said. It's a pleasure."
  res = extract_sentences(text, normalizer)

  assert res == "\"Hello World!\" she said.\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_question_mark():
  text = "\"Hello World?\" she asked. It's a pleasure."
  res = extract_sentences(text, normalizer)

  assert res == "\"Hello World?\" she asked.\nIt's a pleasure."


def test_extract_sentences__space_double_hyphen_space_between_sentences():
  text = "Hello World! -- You look good."
  res = extract_sentences(text, normalizer)

  assert res == "Hello World!\nYou look good."


def test_extract_sentences__sentence_in_brackets():
  text = "Hello World! (Yes, he said that.) You look good."
  res = extract_sentences(text, normalizer)

  assert res == "Hello World!\n(Yes, he said that.)\nYou look good."


def test_extract_sentences__bugfix():
  text = "On one side the titanic forces of nature, inexorable, eternal; on the other the man, frail of body, the creature of an hour, matching himself against them. \"'Fire! Fire!'"
  res = extract_sentences(text, normalizer)

  assert res == "On one side the titanic forces of nature, inexorable, eternal; on the other the man, frail of body, the creature of an hour, matching himself against them.\n'Fire!\nFire!'"


def test_remove_quotation_marks_in_line_if_uneven_number_of_them():
  text = "\"Hello!\n\"Hello World\", she said.\""
  res = remove_quotation_marks_in_line_if_uneven_number_of_them(text)

  assert res == "Hello!\nHello World, she said."
