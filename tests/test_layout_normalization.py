from english_text_normalization.adjustments.layout_normalization import (
    add_dot_after_headings, insert_space_before_and_after_double_hyphen, normalize_three_and_four_dots,
    remove_illustrations, remove_linebreaks, remove_numbers_in_square_brackets,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_underscore_characters)

# region add_dot_after_headings


def test_add_dot_after_headings():
  text = "\nCROSSING THE ISTHMUS\n"
  res = add_dot_after_headings(text)

  assert res == "\nCROSSING THE ISTHMUS.\n"


def test_add_dot_after_headings__dot_already_there_not_added():
  text = "\nCROSSING THE ISTHMUS.\n"
  res = add_dot_after_headings(text)

  assert res == text

# endregion

# region remove_linebreaks


def test_remove_linebreaks():
  text = "Hello\nWorld"
  res = remove_linebreaks(text)

  assert res == "Hello World"

# endregion

# region normalize_three_and_four_dots


def test_normalize_three_and_four_dots__between_two_sentences__no_quotation_marks():
  text = "Hello. ... World."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello. World."


def test_normalize_three_and_four_dots__between_two_sentences__quotation_mark_on_left_side():
  text = "\"Hello.\"... World."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "\"Hello.\" World."


def test_normalize_three_and_four_dots__between_two_sentences__quotation_mark_on_right_side():
  text = "Hello. ... \"World.\""
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello. \"World.\""


def test_normalize_three_and_four_dots__between_two_sentences__quotation_marks_on_both_sides():
  text = "\"Hello.\"... \"World.\""
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "\"Hello.\" \"World.\""


def test_normalize_three_and_four_dots__mid_sentence():
  text = "Hello ... world."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello world."


def test_normalize_three_and_four_dots__end_of_sentence__three_dots():
  text = "Hello world..."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello world."


def test_normalize_three_and_four_dots__end_of_sentence__four_dots():
  text = "Hello world...."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello world."

# endregion

# region remove_numbers_in_square_brackets


def test_remove_numbers_in_square_brackets():
  text = "Hello World[123]"
  res = remove_numbers_in_square_brackets(text)

  assert res == "Hello World"


def test_remove_numbers_in_square_brackets__two_occurences():
  text = "Hello[1] World[2]"
  res = remove_numbers_in_square_brackets(text)

  assert res == "Hello World"


def test_remove_numbers_in_square_brackets__only_empty_square_brackets():
  text = "Hello[] World"
  res = remove_numbers_in_square_brackets(text)

  assert res == text

# endregion

# region remove_illustrations


def test_remove_illustrations():
  #text = "Hello World [Illustration: THE SAVOY FROM THE THAMES, 1650.]"
  text = "I was conducted by a  [Illustration: _Entrance to Mrs. Fry's Ward._]  decently-dressed person, the newly-appointed yards-woman, to the door of a ward where at the head of a long table sat a lady belonging to the Society of Friends."
  res = remove_illustrations(text)

  assert res == "I was conducted by a    decently-dressed person, the newly-appointed yards-woman, to the door of a ward where at the head of a long table sat a lady belonging to the Society of Friends."


def test_remove_illustrations__no_further_information_in_brackets():
  text = "They arrested all known offenders whom they met with,  [Illustration]  and were fully armed for their own and the public protection."
  res = remove_illustrations(text)

  assert res == "They arrested all known offenders whom they met with,    and were fully armed for their own and the public protection."

# endregion

# region remove_underscore_character


def test_remove_repeated_spaces():
  text = " Hello   World  "
  res = remove_repeated_spaces(text)

  assert res == " Hello World "


def test_remove_underscore_characters():
  text = "_Hello_ World"
  res = remove_underscore_characters(text)

  assert res == "Hello World"

# endregion

# region remove_quotation_marks_when_used_as_itemization


def test_remove_quotation_marks_when_used_as_itemization():
  text = "\"The arrival of the English in California being soon known through the\ncountry, two persons in the character of ambassadors came to the Admiral\nand informed him, in the best manner they were able, that the king would\nvisit him, if he might be assured of coming in safety. Being satisfied\non this point, a numerous company soon appeared, in front of which was a\nvery comely person bearing a kind of sceptre, on which hung two crowns,\nand three chains of great length. The chains were of bones, and the\ncrowns of network, curiously wrought with feathers of many colors.\n\n\"Next to sceptre-bearer came the king, a handsome, majestic person,\nsurrounded by a number of tall men dressed in skins, who were followed\nby the common people, who, to make the grander appearance, had painted\ntheir faces of various colors; and all of them, even the children, being\nloaded with presents.\n\n"
  res = remove_quotation_marks_when_used_as_itemization(text)

  assert res == "The arrival of the English in California being soon known through the\ncountry, two persons in the character of ambassadors came to the Admiral\nand informed him, in the best manner they were able, that the king would\nvisit him, if he might be assured of coming in safety. Being satisfied\non this point, a numerous company soon appeared, in front of which was a\nvery comely person bearing a kind of sceptre, on which hung two crowns,\nand three chains of great length. The chains were of bones, and the\ncrowns of network, curiously wrought with feathers of many colors.\n\nNext to sceptre-bearer came the king, a handsome, majestic person,\nsurrounded by a number of tall men dressed in skins, who were followed\nby the common people, who, to make the grander appearance, had painted\ntheir faces of various colors; and all of them, even the children, being\nloaded with presents.\n\n"


def test_remove_quotation_marks_when_used_as_itemization_do_not_match_because_is_quotation():
  text = "\n\n\"Hello world!\" is what the computer said.\n\nI replied \"alright\".\n\n"
  res = remove_quotation_marks_when_used_as_itemization(text)

  assert res == text

# endregion

# region insert_space_before_and_after_double_hyphen


def test_insert_space_before_and_after_double_hyphen():
  text = "It was not likely that a system which left innocent men--for the great bulk of new arrivals were still untried--to be pitchforked by chance anywhere"
  res = insert_space_before_and_after_double_hyphen(text)

  assert res == "It was not likely that a system which left innocent men -- for the great bulk of new arrivals were still untried -- to be pitchforked by chance anywhere"


def test_insert_space_before_and_after_double_hyphen__do_not_replace_as_capital_letter_for_double_hyphen():
  text = "D--n seize you all."
  res = insert_space_before_and_after_double_hyphen(text)

  assert res == text

# endregion

