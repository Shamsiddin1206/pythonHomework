import shift
# Task 1
list = input("Enter a list: ")
element = input("Enter an element: ")
print(list.count(element))

# Task 2
arr = list(map(int, input("Enter only numbers separated by spaces: ").split()))
print(sum(arr))

# Task 3
arr = list(map(int, input("Enter only numbers separated by spaces: ").split()))
print(max(arr))

# Task 4
arr = list(map(int, input("Enter only numbers separated by spaces: ").split()))
print(min(arr))

# Task 5
arr = list(input("Enter elements separated spaces: ").split())
element = input("Element: ")
print(element in arr)

# Task 6
arr = list(input("Enter elements separated spaces: ").split())
print(arr[0] if arr else None)

# task 7
arr = list(input("Enter elements separated spaces: ").split())
print(arr[-1] if arr else None)

# Task 8
arr = list(input("Enter elements separated spaces: ").split())
arr2 = arr[:3]
print(arr2)

# task 9
arr = list(input("Enter elements separated spaces: ").split())
print(arr[::-1])

# Task 10
arr = list(map(int, input("Enter only numbers separated spaces: ").split()))
sortedList = sorted(arr)
print(sortedList)

# Task 11
arr = list(input("Enter elements separated spaces: ").split())
newArr = list(dict.fromkeys(arr))
print(newArr)

# Task 12
arr = list(input("Enter elements separated spaces: ").split())
element = input("element: ")
index = int(input("index of element: "))
arr.insert(index, element)
print(arr)

# Task 13
arr = list(input("Enter elements separated spaces: ").split())
element = input("element: ")
print(arr.index(element) if element in arr else None)

# Task 14
arr = list(input("Enter elements separated spaces: ").split())
print("Not empty" if arr else "Empty")

# task 15
arr = list(map(int, input("Enter elements separated spaces: ").split()))
count = 0
for i in arr:
    if i%2==0:
        count+=1
print(count)

# task 16
arr = list(map(int, input("Enter elements separated spaces: ").split()))
count = 0
for i in arr:
    if i%2!=0:
        count+=1
print(count)

# task 17
arr1 = list(input("Enter elements separated spaces: ").split())
arr2 = list(input("Enter elements separated spaces: ").split())
final = arr1 + arr2
print(final)

# task 18
arr1 = list(input("Enter elements separated spaces: ").split())
arr2 = list(input("Enter elements separated spaces: ").split())
result = False
if not arr2:  # Edge case: empty list is always a sublist
    result = True
else:
    for i in range(len(arr1)-len(arr2)+1):
        if arr1[i:i+len(arr2)] == arr2:
            result = True
            break
print(result)

# task 19
arr1 = list(input("Enter elements separated spaces: ").split())
element1 = input("element: ")
element2 = input("new element: ")
if element1 in arr1:
    arr1[arr1.index(element1)] = element2
print(arr1)


# task 20
arr = list(map(int, input("Enter elements separated spaces: ").split()))
arr1 = sorted(set(arr))
print(arr1[-2])

# task 21
arr = list(map(int, input("Enter elements separated spaces: ").split()))
arr1 = sorted(set(arr))
print(arr1[1])

# Task 22
arr = list(map(int, input("Enter elements separated spaces: ").split()))
arr1 = []
for i in arr:
    if i%2==0:
        arr1.append(i)
print(arr1)

# task 23
arr = list(map(int, input("Enter elements separated spaces: ").split()))
arr1 = []
for i in arr:
    if i%2!=0:
        arr1.append(i)
print(arr1)

# task 24
arr = list(input("Enter elements separated spaces: ").split())
print(len(arr))

# task 25
arr = list(input("Enter elements separated spaces: ").split())
arr1 = arr.copy()
print(arr1)

# task 26
arr = list(map(int, input("Enter elements separated spaces: ").split()))
if len(arr)%2==0:
    print(arr[len(arr)/2], arr[len(arr)/2-1])
else:
    print(arr[(len(arr)-1)/2])

# task 27
arr = list(map(int, input("Enter elements separated spaces: ").split()))
start = int(input("start index of sublist: "))
end = int(input("end index of sublist: "))
print(max(arr[start:end]) if arr[start:end] else None)

# task 28
arr = list(map(int, input("Enter elements separated spaces: ").split()))
start = int(input("start index of sublist: "))
end = int(input("end index of sublist: "))
print(min(arr[start:end]) if arr[start:end] else None)

# task 29
arr = list(input("Enter elements separated spaces: ").split())
ind = int(input("enter index: "))
if ind<len(arr):
    del arr[ind]
else:
    print("Index not found")

# task 30
arr = list(map(int, input("Enter elements separated spaces: ").split()))
arr1 = sorted(arr)
print(arr==arr1)

# task 31
arr = list(map(int, input("Enter elements separated spaces: ").split()))
number = int(input("number of repetition: "))
arr1 = []
for i in arr:
    for _ in range(number):
        arr1.append(i)
print(arr1)


# task 32
arr1 = list(map(int, input("Enter elements separated spaces: ").split()))
arr2 = list(map(int, input("Enter elements separated spaces: ").split()))
arr = sorted(arr1+arr2)
print(arr)

# task 33
arr = list(map(int, input("Enter elements separated spaces: ").split()))
element = input("element: ")
print(i for i, x in enumerate(arr) if x == element)

# task 34
def rotate_list(arr, k):
    k = k % len(arr)  # Handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]
arr = list(map(int, input("Enter elements separated spaces: ").split()))
number = int(input("number of elements for rotation: "))
print(rotate_list(arr, number))

# task 35
number = int(input("number: "))
arr = []
for i in range(1, number+1):
    arr.append(i)
print(arr)

# task 36
arr = list(map(int, input("Enter elements separated spaces: ").split()))
sum = 0
for i in arr:
    if i>=0:
        sum+=i
print(sum)

# task 37
arr = list(map(int, input("Enter elements separated spaces: ").split()))
sum = 0
for i in arr:
    if i<0:
        sum+=i
print(sum)

# task 38
arr = list(map(int, input("Enter elements separated spaces: ").split()))
print(arr == arr[::-1])

# task 39
arr = list(map(int, input("Enter elements separated spaces: ").split()))
number = int(input("number: "))
arr1 = [arr[i:i+number] for i in range(0, len(arr), number)]
print(arr1)

# task 40
arr = list(input("Enter elements separated spaces: ").split())
arr1 = dict.fromkeys(arr)
print(arr1)
