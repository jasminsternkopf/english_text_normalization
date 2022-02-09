from english_text_normalization.sentence_extraction import (
    extract_sentences, remove_quotation_marks_in_line_if_uneven_number_of_them)

def test_extract_sentences__dot():
  text = "Hello World. It's a pleasure."
  res = extract_sentences(text)
  res = extract_sentences(text)

  assert res == "Hello World.\nIt's a pleasure."


def test_extract_sentences__exclamation_mark():
  text = "Hello World! It's a pleasure."
  res = extract_sentences(text)

  assert res == "Hello World!\nIt's a pleasure."


def test_extract_sentences__question_mark():
  text = "Hello World? It's a pleasure."
  res = extract_sentences(text)

  assert res == "Hello World?\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_dot():
  text = "\"Hello World.\" she said. It's a pleasure."
  res = extract_sentences(text)

  assert res == "\"Hello World.\" she said.\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_exclamation_mark():
  text = "\"Hello World!\" she said. It's a pleasure."
  res = extract_sentences(text)

  assert res == "\"Hello World!\" she said.\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_question_mark():
  text = "\"Hello World?\" she asked. It's a pleasure."
  res = extract_sentences(text)

  assert res == "\"Hello World?\" she asked.\nIt's a pleasure."


def test_extract_sentences__contains_abbreviation():
  text = "Hello Doctor Doe, how are you?"
  res = extract_sentences(text)

  assert res == text


def test_extract_sentences__contains_single_letters_with_dot():
  text = "What time is it? \"It's 3 P.M., Sir.\""
  res = extract_sentences(text)

  assert res == "What time is it?\n\"It's 3 P M, Sir.\""


def test_extract_sentences__double_hyphen_between_sentences():
  text = "Hello World!--You look good."
  res = extract_sentences(text)

  assert res == "Hello World!\nYou look good."


def test_extract_sentences__three_dots_between_sentences():
  text = "Hello World!...You look good."
  res = extract_sentences(text)

  assert res == "Hello World!\nYou look good."


def test_extract_sentences__three_dots_between_sentences_and_the_first_one_ends_with_dot():
  text = "Hello World....You look good."
  res = extract_sentences(text)

  assert res == "Hello World.\nYou look good."


def test_remove_quotation_marks_in_line_if_uneven_number_of_them():
  text = "\"Hello!\n\"Hello World\", she said.\""
  res = remove_quotation_marks_in_line_if_uneven_number_of_them(text)

  assert res == "Hello!\nHello World, she said."
