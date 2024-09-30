l = 'NamasteIndia'
a =''.join(set(l))
result_upper = ''.join(map(str.upper, a))
result_lower = ''.join(map(str.lower, a))
print("Uppercase:", result_upper)
print("Lowercase:", result_lower)