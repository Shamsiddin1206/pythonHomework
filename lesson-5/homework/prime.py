def is_prime():
    n = int(input("Enter a number: "))
    a = 0
    if 2 > n:
        print("False")
        return False
    for i in range(2, n+1):
        if n % i == 0:
            a+=1
    if a==1:
        print("True")
        return True
    print("False")
    return False

# Example usage:
is_prime()