from code_challenges.insertion_sort import insertion_sort

list_one = [8, 3, 5]
list_two = [9, 6, 3]
list_three = [5, 8, 5, 2, 5, 7, 5]
list_four = [4, -1, 8, 10, -9]

def test_insertion_sort_exists():
  assert insertion_sort

def test_sort_random():
  actual = insertion_sort(list_one)
  expected = [3, 5, 8]
  assert actual == expected

def test_sort_reversed():
  actual = insertion_sort(list_two)
  expected = [3,6,9]
  assert actual == expected

def test_sort_duplicates():
  actual = insertion_sort(list_three)
  expected = [2,5,5,5,5,7,8]
  assert actual == expected

def test_negative():
  actual = insertion_sort(list_four)
  expected = [-9, -1, 4, 8, 10]
  assert actual == expected


