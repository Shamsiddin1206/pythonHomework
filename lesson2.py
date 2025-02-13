#NUMBER DATA TYPE QUESTIONS

#Task 1
# num = float(input("number: "))
# print(round(num, 2))

#Task 2
# nums = []
# for i in range(3):
#     nums.append(input("number: "))
# print("Max: " + max(nums) + "; Min: " + min(nums))

#Task 3
# n = int(input("Enter in km: "))
# print("In m: ", (n * 1000))
# print("In cm: ", n*100000)

# Task 4
# a = int(input("a: "))
# b = int(input("b: "))
# print(a//b)
# print(a%b)

# Task 5
# print(float(input("Celsius: "))*9/5+32)

# Task 6
# print(int(input("Number: ")) % 10)

# Task 7
# print("Even" if int(input("Number: "))%2==0 else "Odd")

# -------------------------------------------------------------

# STRING QUESTIONS
# Task 1
# name = input("Enter your name: ")
# birth_year = int(input("Enter your year of birth: "))
# print(f"{name} you are {2025 - birth_year} years old")

# Task 2
# print("Malibu")

# Task 3
# s = (input("text: "))
# print(f"length: {len(s)}, Uppercase: {s.upper()}, Lower: {s.lower()}")

# Text 4
# s = input("number: ")
# print("Palindrome" if s[0] == s[len(s)-1] else "Not a Palindrome")

# Text 5
# s = input("text: ").lower()
# vowels = "aeuio"
# v = 0
# c = 0
# for i in s:
#     if (i in vowels):
#         v+=1
#     else:
#         c+=1
# print(f"vowels: {v}, const: {c}")

# Task 6
# s1 = input("text 1: ")
# s2 = input("text 2: ")
# print("Yes" if (s1 in s2) or (s2 in s1) else "Odd")

# Task 7
# s = input("Enter a sentence: ")
# old, new = input("Replace: "), input("With: ")
# print(s.replace(old, new))

# Task 8
# s = input("text: ")
# print(f"First: {s[0]}, Last: {s[-1]}")

# Task 9
# print(input("Enter a string: ")[::-1])

# Task 10
# s = input("text: ")
# print(len(s.split()))

# Task 11
# s = input("Any: ")
# for i in s:
#     if i.isdigit():
#         print("Yes, Digit")
#         break
#     else:
#         print("No")

# Task 12
# print(input("text: ").replace(" ", ","))

# Task 13
# print(input("Text: ").replace(" ", ""))

# Task 14
# print("Yes" if input("s1: ") == input("s2: ") else "No")

# Task 15
# s = input("text: ")
# k = s[0]
# for i in range(len(s)):
#     if s[i] == " ":
#         k+=(s[i+1])
# print(k)

# Task 16
# s, char = input("Enter a string: "), input("Enter character: ")
# print(s.replace(char, ""))

# Task 17
# s = input("text: ")
# vowels = "aeuioAEUIO"
# for i in s:
#     if i in vowels:
#         s = s.replace(i, "*")
# print(s)

# Task 18
# s = input("Enter a string: ").split()
# if s:
#     print(f"Starts with: {s[0]}")
#     print(f"Ends with: {s[-1]}")
# else:
#     print("Empty input!")