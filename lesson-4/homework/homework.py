from collections import Counter
import random

# Task 1
list1 = list(map(int, input("List 1: ").split()))
list2 = list(map(int, input("List 2: ").split()))
count1 = Counter(list1)
count2 = Counter(list2)

result = []

for num in count1:
    if num not in count2:
        result.extend([num] * count1[num])

for num in count2:
    if num not in count1:
        result.extend([num] * count2[num])

print(result)

# Task 2
n = int(input("n: "))
for i in range(1, n):
    print(i*i)

# Task 3
txt = input("String: ")
vowels = "aeiouAEIOU"
result = []
i = 0

while i < len(txt):
    result.append(txt[i])
    if (i + 1) % 3 == 0:
        if i + 1 < len(txt):
            if txt[i] in vowels or (i > 0 and txt[i - 1] == '_'):
                if i + 2 < len(txt):
                    result.append(txt[i + 1])
                    result.append('_')
                    vowels += txt[i+1]
                    i += 1
            else:
                result.append('_')
    i += 1

print(''.join(result))

# Task 4
def play_game():
    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            return

        attempts -= 1
        print(f"Attempts left: {attempts}")

    print("You lost. Want to play again?")
    replay = input("Type 'Y', 'YES', 'y', 'yes', 'ok' to play again: ").strip().lower()
    if replay in ('y', 'yes', 'ok'):
        play_game()
    else:
        print("Thanks for playing!")

play_game()

# Task 5
password = input("Enter a password: ")
if len(password) < 8:
    print("Password is too short.")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")

# Task 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range (1, 100):
    if is_prime(i):
        print(i)


