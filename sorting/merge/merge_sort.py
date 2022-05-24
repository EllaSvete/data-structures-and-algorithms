def merge_sort(lst):
  n = len(lst)
  print(f"merge_sort {lst}")
  if n > 1:
    mid = n // 2
    left = lst[:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, lst)
  return lst

def merge(left, right, lst):
  i = j = k = 0

  print(f"merge: left{left}, right{right}")

  while i < len(left) and j < len(right):
    print(f"smallest {left[i:]} and {right[j:]}")

    if left[i] <= right[j]:
      lst[k] = left[i]
      i += 1
    else:
      lst[k] = right[j]
      j += 1
    k += 1

  if i == len(left):
    while j < len(right):
      lst[k] = right[j]
      j += 1
      k += 1
  else:
    while i < len(left):
      lst[k] = left[i]
      i += 1
      k += 1

