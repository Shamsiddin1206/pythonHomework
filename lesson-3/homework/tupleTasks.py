def count_occurrences():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    element = input("Element: ")
    print(arr.count(element))

def max_element():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(max(arr) if arr else None)

def min_element():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(min(arr) if arr else None)

def check_element():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    element = input("Element: ")
    print(element in arr)

def first_element():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr[0] if arr else None)

def last_element():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr[-1] if arr else None)

def tuple_length():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(len(arr))

def slice_tuple():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr[:3])

def concatenate_tuples():
    arr1 = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    arr2 = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr1 + arr2)

def is_tuple_empty():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(len(arr) == 0)

def get_indices():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    element = input("Element: ")
    print([i for i, val in enumerate(arr) if val == element])

def second_largest():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    arr1 = sorted(set(arr))
    arr1.reverse()
    print(arr1[1])

def second_smallest():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    arr1 = sorted(set(arr))
    print(arr1[1])

def single_element_tuple():
    arr = (5,)
    print(arr)

def list_to_tuple():
    arr = list(input("Enter elements separated spaces: ").split())
    arr1 = tuple(arr)
    print(arr1)

def is_sorted():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr == sorted(arr))

def max_of_subtuple():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    start = int(input("start index: "))
    end = int(input("end index: "))
    print(max(arr[start:end]))

def min_of_subtuple():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    start = int(input("start index: "))
    end = int(input("end index: "))
    print(min(arr[start:end]))

def remove_element():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    element = int(input("element: "))
    lst = list(arr)
    if element in lst:
        lst.remove(element)
        arr = tuple(lst)
    print(arr)

def create_nested_tuple():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    n = int(input("n: "))
    arr1 = tuple(arr[i:i+n] for i in range(0, len(arr), n))
    print(arr1)

def repeat_tuple():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    n = int(input("n: "))
    arr1 = []
    for i in arr:
        for _ in range(n):
            arr1.append(i)
    arr1 = type(arr1)
    print(arr1)

def range_tuple():
    arr = tuple(range(1, 11))
    print(arr)

def reverse_tuple():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr[::-1])

def is_palindrome():
    arr = tuple(map(int, input("Enter only numbers separated by spaces: ").split()))
    print(arr == arr[::-1])

def get_unique_elements():
    arr = tuple(input("Enter elements separated spaces: ").split())
    arr1 = tuple(dict.fromkeys(arr))
    print(arr1)

count_occurrences()
max_element()
min_element()
check_element()
first_element()
last_element()
tuple_length()
slice_tuple()
concatenate_tuples()
is_tuple_empty()
get_indices()
second_largest()
second_smallest()
single_element_tuple()
list_to_tuple()
is_sorted()
max_of_subtuple()
min_of_subtuple()
remove_element()
create_nested_tuple()
repeat_tuple()
range_tuple()
reverse_tuple()
is_palindrome()
get_unique_elements()