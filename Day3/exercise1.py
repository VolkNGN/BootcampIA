def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
def is_even(n):
    
    if n % 2 == 0:
        return True
    else:
        return False

def check_even_or_odd(n):
    if is_even(n):
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")

check_even_or_odd(4)
print_factorial(4)