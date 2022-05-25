# Blog Notes: Merge Sort

## Introduction

Today we are walking through how to merge and sort a list!

For us it's easy to visualize how a list of numbers should be put in order. Since computer are dumb, they need some extra helps organizing.

### Visualization

Let's take a look at this (not) beautiful visualization:

[Merge Sort](merge-sort.png)

### Pseudo Code

```{python}
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

### Walk Through

- The first step is to
find the length of the list. If the length of the list is greater than 1 than we are going to divide by 2, and set that to a variable: mid

- we then take the mid, split it and set it to variables right and we do the same to the other side. This results in giving us multiple lists all the length of one number.

- Next, compare each number (or each list) to determine which is the smallest value working our way through each number

- Finally we use merge to *merge* our sub-lists into one final list in our desired order.

### Big O

- Time: O(log(n)): merge sort always divides the list into two halves and takes linear time to merge two halves.
- Space: O(n) because the size of the list is dependent on how many things are in the list.

### Code

```{python}
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
```

Thanks for reading!
