from english_text_normalization.auxiliary_methods.txt_files_reading import \
    get_str_out_of_txt_file


def test_get_str_out_of_txt_file():
  filename = "data/test.txt"
  res = get_str_out_of_txt_file(filename)

  assert res == "abcd\ncdefg"


def test_get_str_out_of_txt_file__sep_is_not_new_line():
  filename = "data/test.txt"
  res = get_str_out_of_txt_file(filename, sep="&")

  assert res == "abcd&cdefg"
