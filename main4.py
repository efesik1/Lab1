my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
keys = list(my_dict.keys())
values = list(my_dict.values())
sorted_values = sorted(values)
smallest_keys = []
for i in range(3):
    smallest_value = sorted_values[i]
    smallest_index = values.index(smallest_value)
    smallest_key = keys[smallest_index]
    smallest_keys.append(smallest_key)
print("Три ключа с самыми маленькими значениями:")
for key in smallest_keys:
    print(key)