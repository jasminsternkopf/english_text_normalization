from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import enchant
from english_text_normalization.auxiliary_methods.txt_files_reading import (
    dump_iterable_in_txt_file, get_list_out_of_txt_file)
from nltk.corpus import names as nltk_names
from nltk.corpus import words as nltk_words


def get_word_variants(names_or_words: Iterable[str]) -> List[Tuple[str]]:
  all_word_variants = []
  for word in names_or_words:
    word_lower = word.lower()
    word_singular = get_singular_of_word(word_lower)
    if word_singular:
      word_variants = (word, word_lower, word_singular)
    else:
      word_variants = (word, word_lower)
    all_word_variants.append(word_variants)
  return all_word_variants


def get_singular_of_word(word: str) -> Optional[str]:
  if word[-1] != "s":
    return None
  if word[-3:-1] == "ie":
    return word[:-3] + "y"
  return word[:-1]


def find_words_in_wordcorpus(names_or_words: Iterable[Tuple[str]]) -> Tuple[List[str], List[str]]:
  words_in_corpus = []
  words_not_in_corpus = []
  for variants_of_a_name in names_or_words:
    name_appended = False
    for name_variante in variants_of_a_name:
      if name_variante in nltk_words.words():
        # words_in_corpus.append(name_variante)
        words_in_corpus.append(variants_of_a_name[0])
        name_appended = True
        break
    if not name_appended:
      words_not_in_corpus.append(variants_of_a_name[0])
  return words_in_corpus, words_not_in_corpus


def find_names_in_namecorpus(names_or_words: Iterable[str]) -> Tuple[List[str], List[str]]:
  words_in_corpus = []
  words_not_in_corpus = []
  for name in names_or_words:
    if name in nltk_names.words():
      words_in_corpus.append(name)
    else:
      words_not_in_corpus.append(name)
  return words_in_corpus, words_not_in_corpus


def build_name_corpus(names_and_words: Iterable[str], exceptions: Iterable[str]) -> Tuple[List[str], List[str]]:
  variants = get_word_variants(names_and_words)
  words, not_words = find_words_in_wordcorpus(variants)
  names, not_names = find_names_in_namecorpus(names_and_words)
  words = set(words).difference(set(names))
  words = list(words)
  neither_words_nor_names = set(not_words).intersection(set(not_names))
  in_british_enchant, not_in_british_enchant = check_with_enchant(neither_words_nor_names, "en_GB")
  in_american_enchant, not_in_american_enchant = check_with_enchant(
    neither_words_nor_names, "en_US")
  not_in_enchant = set(not_in_british_enchant).intersection(set(not_in_american_enchant))
  not_in_enchant = list(not_in_enchant)
  names.extend(not_in_enchant)
  in_enchant = set(in_british_enchant).union(set(in_american_enchant))
  in_enchant -= set(exceptions)
  words.extend(in_enchant)
  names.extend(exceptions)
  return names, words


def our_name_corpus():
  names_or_words = get_list_out_of_txt_file("data/only_names.txt")
  exceptions = get_list_out_of_txt_file("data/exceptions.txt")
  names, words = build_name_corpus(names_or_words, exceptions)
  dump_iterable_in_txt_file(names, Path("data/name_corpus.txt"))
  dump_iterable_in_txt_file(words, Path("data/not_name_corpus.txt"))


def check_with_enchant(words: Iterable[str], dict_tag: str) -> Tuple[List[str], List[str]]:
  enchant_dict = enchant.Dict(dict_tag)
  in_dict = []
  not_in_dict = []
  for word in words:
    if enchant_dict.check(word):
      in_dict.append(word)
    else:
      not_in_dict.append(word)
  return in_dict, not_in_dict
