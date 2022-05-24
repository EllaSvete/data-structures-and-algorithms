def insertion_sort(lst):
  for i in range(len(lst)): #
    j = i-1 # nothing, (0), (1), (2)
    temp = lst[i] # 8, 4, 23, 42


    while j >= 0 and temp < lst[j]:
      # this wont run, it will cayuse j =0 and temp = 4(less than 0 index of list 8)
      # wont run j = 1 and temp = 23 23 > 4 so won't run
      # wont run because 42 is not less than 23

      lst[j+1] = lst[j] #(1)4 = (0)8
      j -= 1 # -1

    lst[j+1] = temp # 8, temp = None?
    # this index is only reassigned if temp is less than the index we are comparing

  return  lst

# [8,4,23,42,16,15]

# iteration 4

# i=4 meaning j= [3] (j = 42)
# temp = list[i] # i = 16
# 16 <42 (true, run loop)
# temp (16) new list [j(2)] 16 < 23
# list[j+1] is (16) = 42, reassigning j+1 value to the value of list[j] (2) value of
# j =- 1 # [3] -1 = [2]

# as long as list [i] is less than lst[j]
