from merge_sort import merge_sort, merge

def test_merge_sort_exists():
  assert merge_sort

def test_merge_exists():
  assert merge


def test_random_sort():
  random_list = [5, 8, 0, 1, 7]
  actual = merge_sort(random_list)
  expected = [0, 1, 5, 7, 8]
  assert actual == expected

def test_negative_integers():
  negative_list = [-1, 8, 13, -5, -9]
  actual = merge_sort(negative_list)
  expected = [-9, -5, -1, 8, 13]
  assert actual == expected

def test_reversed_order():
  reversed_list = [9,8,7,6,5,4]
  actual = merge_sort(reversed_list)
  expected = [4, 5, 6, 7, 8, 9]
  assert actual == expected

def test_duplicates():
  duplicates_list = [7, 7, 7, 5, 3, 2]
  actual = merge_sort(duplicates_list)
  expected = [2,3,5,7,7,7]
  assert actual == expected

def test_floats():
  float_list = [0.6, 0.7, 0.1, 5, 7]
  actual = merge_sort(float_list)
  expected = [0.1, 0.6, 0.7, 5, 7]
  assert actual == expected
