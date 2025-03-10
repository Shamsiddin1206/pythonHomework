import random

def get_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    key = input("Key: ")
    print(d.get(key, None))

def check_key():
    d = eval(input("Enter dictionary (key-value pairs): "))
    key = input("Key: ")
    print(key in d)

def count_keys():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(len(d))

def get_all_keys():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(list(d.keys()))

def get_all_values():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(list(d.values()))

def merge_dicts():
    d1 = eval(input("Enter first dictionary (key-value pairs): "))
    d2 = eval(input("Enter second dictionary (key-value pairs): "))
    d = {**d1, **d2}
    print(d)

def remove_key():
    d = eval(input("Enter dictionary (key-value pairs): "))
    key = input("Key: ")
    d.pop(key, None)
    print(d)

def clear_dict():
    d = eval(input("Enter dictionary (key-value pairs): "))
    d.clear()
    print(d)

def is_dict_empty():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(len(d) == 0)

def get_key_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    key = input("Key: ")
    print((key, d[key]) if key in d else None)

def update_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    key = input("Key: ")
    value = input("New Value: ")
    d[key] = value
    print(d)

def count_value_occurrences():
    d = eval(input("Enter dictionary (key-value pairs): "))
    value = input("Value: ")
    print(list(d.values()).count(value))

def invert_dict():
    d = eval(input("Enter dictionary (key-value pairs): "))
    d_inverted = {v: k for k, v in d.items()}
    print(d_inverted)

def find_keys_with_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    value = input("Value: ")
    keys = [k for k, v in d.items() if v == value]
    print(keys)

def create_dict_from_lists():
    keys = input("Enter keys separated by spaces: ").split()
    values = input("Enter values separated by spaces: ").split()
    d = dict(zip(keys, values))
    print(d)

def has_nested_dict():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(any(isinstance(v, dict) for v in d.values()))

def get_nested_value():
    d = eval(input("Enter nested dictionary (key-value pairs): "))
    key1 = input("Outer Key: ")
    key2 = input("Inner Key: ")
    print(d.get(key1, {}).get(key2, None))

def create_default_dict():
    from collections import defaultdict
    default_value = input("Enter default value: ")
    d = defaultdict(lambda: default_value)
    print(d)

def count_unique_values():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(len(set(d.values())))

def sort_dict_by_key():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(dict(sorted(d.items())))

def sort_dict_by_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(dict(sorted(d.items(), key=lambda item: item[1])))

def filter_dict_by_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    value = input("Filter Value: ")
    filtered = {k: v for k, v in d.items() if v == value}
    print(filtered)

def check_common_keys():
    d1 = eval(input("Enter first dictionary (key-value pairs): "))
    d2 = eval(input("Enter second dictionary (key-value pairs): "))
    print(set(d1.keys()) & set(d2.keys()))

def create_dict_from_tuple():
    t = eval(input("Enter list of tuples (key-value pairs): "))
    print(dict(t))

def get_first_key_value():
    d = eval(input("Enter dictionary (key-value pairs): "))
    print(next(iter(d.items()), None))


get_value()
check_key()
count_keys()
get_all_keys()
get_all_values()
merge_dicts()
remove_key()
clear_dict()
is_dict_empty()
get_key_value()
update_value()
count_value_occurrences()
invert_dict()
find_keys_with_value()
create_dict_from_lists()
has_nested_dict()
get_nested_value()
create_default_dict()
count_unique_values()
sort_dict_by_key()
sort_dict_by_value()
filter_dict_by_value()
check_common_keys()
create_dict_from_tuple()
get_first_key_value()
