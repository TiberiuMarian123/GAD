list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# sort the list ascending
list_ascend = sorted(list)
print("list ascending:", list_ascend)

# sort the list descending
list_descend = sorted(list, reverse = True)
print("List descending: ", list_descend)

# just the even numbers from the sorted list
list_even = list_ascend[1:10:2]
print("Even numbers sorted list:", list_even)

# or... the even numbers from the unsorted list
list_even_unsorted = list[1:4:2] + list[6:8] + list[9:10]
print("Even numbers unsorted list:", list_even_unsorted)

# just the odd numbers from the sorted list
list_odd = list_ascend[:9:2]
print("Odd numbers sorted list: ", list_odd)

# or print the odd numbers from the unsorted list
list_odd_unsorted = list[:5:2] + list[5:9:3]
print("Odd numbers unsorted list: ", list_odd_unsorted)

# print multiple of 3 elements
list_multiple_3 = list[2:5:2] + list[9:10]
print("Multiple of 3 from unsorted list: ", list_multiple_3)
