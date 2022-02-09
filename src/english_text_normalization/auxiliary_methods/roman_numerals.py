from typing import List



def roman_numerals_for_a_certain_power_of_ten(power_of_ten: str, five_times_power_of_ten: str, next_power_of_ten: str) -> List[str]:
  all_numerals = []
  for no_of_five_times_power_of_ten in range(2):
    for no_of_power_of_ten in range(4):
      roman_numeral = five_times_power_of_ten * \
        no_of_five_times_power_of_ten + power_of_ten * no_of_power_of_ten
      all_numerals.append(roman_numeral)
    if no_of_five_times_power_of_ten == 0:
      all_numerals.append(power_of_ten + five_times_power_of_ten)
  all_numerals.append(power_of_ten + next_power_of_ten)
  return all_numerals


def roman_units() -> List[str]:
  return roman_numerals_for_a_certain_power_of_ten("I", "V", "X")


def roman_tens() -> List[str]:
  return roman_numerals_for_a_certain_power_of_ten("X", "L", "C")


def get_all_roman_numerals_up_to_N(N: int = 99) -> List[str]:
  assert N > 0
  assert N < 100
  units = roman_units()
  tens = roman_tens()
  all_combinations = [ten + unit for ten in tens for unit in units]
  return all_combinations[1:N + 1]
