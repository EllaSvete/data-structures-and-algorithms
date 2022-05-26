import pytest
from code_challenges.roman_numerals import convert_char, roman_numerals

def test_convert_char_exists():
  assert convert_char

def test_roman_numerals_exists():
  assert roman_numerals

def test_check_conversion():
  roman_test = roman_numerals('CXLII')
  assert str(roman_test) == '142'

def test_longer_number():
  roman_test = roman_numerals('MCMLXXIV')
  assert str(roman_test) == '1974'

def test_duplicate_numbers():
  roman_test = roman_numerals('MDCCLXXIV')
  assert str(roman_test) == '1774'

def test_one_number():
  roman_test = roman_numerals('X')
  assert str(roman_test) == '10'

def test_lower_case():
  roman_test = roman_numerals(str.upper('x'))
  assert str(roman_test) == '10'
