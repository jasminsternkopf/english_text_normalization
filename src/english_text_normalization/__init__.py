from english_text_normalization.adjustments import (
    add_dot_after_headings, add_the_between_king_name_and_roman_numeral,
    change_p_dot_before_number_into_page, expand_abbreviations,
    expand_and_a_half, expand_units_of_measure, geo_to_george, get_dot_regex,
    insert_space_before_and_after_double_hyphen, normalize_all_units,
    normalize_am_and_pm, normalize_degrees_minutes_and_seconds,
    normalize_double_quotation_marks, normalize_emails_and_at,
    normalize_latitude_and_longitude, normalize_length_units,
    normalize_numbers, normalize_our_king_names, normalize_percent,
    normalize_point_before_numbers, normalize_pounds_shillings_and_pence,
    normalize_second_and_third_when_abbr_with_d,
    normalize_single_quotation_marks_and_apostrophes,
    normalize_temperatures_celsius, normalize_temperatures_fahrenheit,
    normalize_temperatures_general, normalize_three_and_four_dots,
    normalize_time_units, normalize_today_and_tomorrow, normalize_weight_units,
    remove_colon_in_digital_time_format,
    remove_dot_after_single_capital_letters,
    remove_dot_after_single_small_letters, remove_dot_between_word_and_number,
    remove_double_hyphen_before_or_after_colon, remove_equal_sign,
    remove_everything_in_square_brackets, remove_four_hyphens,
    remove_illustrations, remove_linebreaks, remove_numbers_in_square_brackets,
    remove_plus, remove_quotation_marks_when_used_as_itemization,
    remove_repeated_spaces, remove_sic, remove_stars, remove_tilde,
    remove_underscore_characters, replace_and_sign_with_word_and,
    replace_at_symbols, replace_big_letter_abbreviations,
    replace_eg_with_for_example, replace_etc_with_et_cetera,
    replace_four_hyphens_by_two, replace_hyphen_between_numbers_with_to,
    replace_ie_with_that_is, replace_mail_addresses, replace_no_with_number,
    replace_nos_with_numbers, replace_vg_with_for_instance,
    write_out_month_abbreviations)
from english_text_normalization.sentence_extraction import extract_sentences
