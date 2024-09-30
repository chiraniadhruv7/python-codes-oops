list_of_integers = [1, 2, 3]
tuple_of_integers = (4, 5, 6)

result = list(map(str, list_of_integers)) + list(map(str, tuple_of_integers))

print(result)
