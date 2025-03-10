import random

def union_sets():
    s1 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s2 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s = s1 | s2
    print(s)

def intersection_sets():
    s1 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s2 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s = s1 & s2
    print(s)

def difference_sets():
    s1 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s2 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s = s1 - s2
    print(s)

def is_subset():
    s1 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s2 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(s1 <= s2)

def check_element():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(input("n: "))
    print(n in s)

def set_length():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(len(s))

def list_to_set():
    arr = list(map(int, input("Enter elements separated spaces: ").split()))
    s = set(arr)
    print(s)

def remove_element():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(input("n: "))
    s.discard(n)
    print(s)

def clear_set():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s.clear()
    print(s)

def is_empty_set():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(len(s) == 0)

def symmetric_difference_sets():
    s1 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s2 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s = s1 ^ s2
    print(s)

def add_element():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(input("n: "))
    s.add(n)
    print(s)

def pop_element():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(s.pop() if s else None)

def max_element():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(max(s) if s else None)

def min_element():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(min(s) if s else None)

def filter_even():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s1 = {x for x in s if x % 2 == 0}
    print(s1)

def filter_odd():
    s = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s1 = {x for x in s if x % 2 != 0}
    print(s1)

def create_range_set():
    start = int(input("start: "))
    end = int(input("end: "))
    s = set(range(start, end + 1))
    print(s)

def merge_lists():
    arr1 = list(map(int, input("Enter elements separated spaces: ").split()))
    arr2 = list(map(int, input("Enter elements separated spaces: ").split()))
    s = set(arr1 + arr2)
    print(s)

def are_disjoint():
    s1 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    s2 = set(map(int, input("Enter numbers separated by spaces: ").split()))
    print(s1.isdisjoint(s2))


def remove_duplicates():
    arr = list(map(int, input("Enter elements separated spaces: ").split()))
    s = set(arr)
    arr1 = list(s)
    print(arr1)

def count_unique():
    arr = list(map(int, input("Enter elements separated spaces: ").split()))
    print(len(set(arr)))

def generate_random_set():
    size = int(input("size: "))
    start = int(input("start: "))
    end = int(input("end: "))
    s = {random.randint(start, end) for _ in range(size)}
    print(s)

union_sets()
intersection_sets()
difference_sets()
is_subset()
check_element()
set_length()
list_to_set()
remove_element()
clear_set()
is_empty_set()
symmetric_difference_sets()
add_element()
pop_element()
max_element()
min_element()
filter_even()
filter_odd()
create_range_set()
merge_lists()
are_disjoint()
remove_duplicates()
count_unique()
generate_random_set()