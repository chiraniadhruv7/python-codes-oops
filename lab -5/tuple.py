tuple_of_integers = (10, 20, 30, 40, 50)
string_value = "100"

selected_elements = (tuple_of_integers[1], tuple_of_integers[3])
new_list = list(map(str, selected_elements)) + [int(string_value)]

print(new_list)
