list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

common_items = list(set(list1) & set(list2))
common_sum = sum(common_items)

print("Common items:", common_items)
print("Sum of common items:", common_sum)