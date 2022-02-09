from english_text_normalization.adjustments.normalize_degrees import (
    normalize_degrees_minutes_and_seconds, normalize_temperatures_celsius,
    normalize_temperatures_fahrenheit)

# region normalize_temperatures_celsius


def test_normalize_temperatures_celsius():
  text = "It was 30 deg.C. outside today."
  res = normalize_temperatures_celsius(text)

  assert res == "It was 30 degrees Celsius outside today."


def test_normalize_temperatures_celsius__2():
  text = "Today it was 30 deg C!"
  res = normalize_temperatures_celsius(text)

  assert res == "Today it was 30 degrees Celsius!"

# endregion

# region normalize_temperatures_fahrenheit


def test_normalize_temperatures_fahrenheit__f_not_fahr():
  text = "It was 30 deg.F. outside today."
  res = normalize_temperatures_fahrenheit(text)

  assert res == "It was 30 degrees Fahrenheit outside today."


def test_normalize_temperatures_fahrenheit__f_not_fahr__2():
  text = "Today it was 30 deg F!"
  res = normalize_temperatures_fahrenheit(text)

  assert res == "Today it was 30 degrees Fahrenheit!"


def test_normalize_temperatures_fahrenheit__fahr_not_f():
  text = "It was 30 deg.Fahr. outside today."
  res = normalize_temperatures_fahrenheit(text)

  assert res == "It was 30 degrees Fahrenheit outside today."


def test_normalize_temperatures_fahrenheit__fahr_not_f__2():
  text = "Today it was 30 deg Fahr!"
  res = normalize_temperatures_fahrenheit(text)

  assert res == "Today it was 30 degrees Fahrenheit!"


def test_normalize_temperatures_fahrenheit__fah_not_f_or_fahr():
  text = "It was 30 deg.Fah. outside today."
  res = normalize_temperatures_fahrenheit(text)

  assert res == "It was 30 degrees Fahrenheit outside today."

# endregion

# region normalize_degrees_minutes_and_seconds


def test_normalize_degrees_minutes_and_seconds__only_minutes_and_sconds():
  text = "My house is at longitude 12 degrees 4' 3\"."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees 4 minutes 3 seconds."


def test_normalize_degrees_minutes_and_seconds__with_one_half():
  text = "My house is at longitude 12 degrees 4' 3-1/2\"."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees 4 minutes 3-1/2 seconds."


def test_normalize_degrees_minutes_and_seconds__degrees_minutes_and_sconds():
  text = "My house is at longitude 12 deg. 4' 3\"."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees 4 minutes 3 seconds."


def test_normalize_degrees_minutes_and_seconds__with_commata():
  text = "My house is at longitude 12 deg., 4', 3\"."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees, 4 minutes 3 seconds."


def test_normalize_degrees_minutes_and_seconds__only_degrees_and_sconds():
  text = "My house is at longitude 12 deg. 3\"."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees 3 seconds."


def test_normalize_degrees_minutes_and_seconds__with_west_as_word():
  text = "My house is at longitude 12 deg. 3\" West."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees 3 seconds West."


def test_normalize_degrees_minutes_and_seconds__with_w():
  text = "My house is at longitude 12 deg. 3\" W."
  res = normalize_degrees_minutes_and_seconds(text)

  assert res == "My house is at longitude 12 degrees 3 seconds West"

# endregion
