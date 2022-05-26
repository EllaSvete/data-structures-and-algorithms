def convert_char(roman_char):
  conversion = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
  }

  return conversion.get(roman_char, 0)

# CXLII

def roman_numerals(roman):
  total= 0


  for i in range(len(roman)-1):
    left_char = roman[i]
    print(f"left char:{left_char}")


    right_char = roman[i+1]
    print(f"right char: {right_char}")

    left_value = convert_char(left_char)
    print(f"convert {left_value}")

    right_value = convert_char(right_char)
    print(f"convert {right_value}")

    if left_value < right_value:
      left_value = -left_value

    total += left_value
    print(f" total: {total}")

  if roman:
      total += convert_char(roman[-1])
      print(f"total: {total}")

  return total


