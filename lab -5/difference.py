list1 = [10, 20, 30]
list2 = [5, 15, 25]

sum_result = list(map(lambda x, y: x + y, list1, list2))
difference_result = list(map(lambda x, y: x - y, list1, list2))

print("Sum:", sum_result)
print("Difference:", difference_result)
