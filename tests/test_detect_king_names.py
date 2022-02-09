from english_text_normalization.auxiliary_methods.detect_king_names import (
    find_words_in_wordcorpus, get_singular_of_word, get_word_variants)


def test_get_singular_of_word():
  word = "chapters"
  res = get_singular_of_word(word)

  assert res == "chapter"


def test_get_singular_of_word__input_is_singular():
  word = "chapter"
  res = get_singular_of_word(word)

  assert res is None


def test_get_singular_of_word__input_is_singular__2():
  word = "discovery"
  res = get_singular_of_word(word)

  assert res is None


def test_get_singular_of_word__word_ends_with_ies():
  word = "discoveries"
  res = get_singular_of_word(word)

  assert res == "discovery"


def test_get_name_variants():
  names = ["Hello", "World"]
  res = get_word_variants(names)

  assert res == [("Hello", "hello"), ("World", "world")]


def test_get_name_variants__2():
  names = ["Chapters", "Discoveries"]
  res = get_word_variants(names)

  assert res == [("Chapters", "chapters", "chapter"), ("Discoveries", "discoveries", "discovery")]


def test_find_words_in_wordcorpus():
  names = ["Chapters", "Discoveries"]
  variants = get_word_variants(names)
  res_1, res_2 = find_words_in_wordcorpus(variants)

  assert res_1 == ["Chapters", "Discoveries"]
  assert not res_2


def test_find_words_in_wordcorpus__2():
  names = ["Chapter", "Aaron"]
  variants = get_word_variants(names)
  res_1, res_2 = find_words_in_wordcorpus(variants)

  assert res_1 == ["Chapter", "Aaron"]
  assert not res_2


def test_find_words_in_wordcorpus__word_not_in_corpus():
  names = ["Krtzkrz"]
  variants = get_word_variants(names)
  res_1, res_2 = find_words_in_wordcorpus(variants)

  assert not res_1
  assert res_2 == ["Krtzkrz"]
