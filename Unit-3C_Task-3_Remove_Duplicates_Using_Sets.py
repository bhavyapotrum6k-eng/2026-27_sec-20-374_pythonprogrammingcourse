my_list = [1, 2, 2, 3, 4, 4, 5, 1, 3]
print("Original list:", my_list)
unique_list = list(set(my_list))
print("After Removing Duplicates:", unique_list)
unique_ordered = list(dict.fromkeys(my_list))
print("Without Changing Order:", unique_ordered)