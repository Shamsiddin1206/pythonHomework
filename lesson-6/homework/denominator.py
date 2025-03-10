def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    print("Output:", div(a, b))
except ValueError:
    print("Invalid input! Please enter integers.")
