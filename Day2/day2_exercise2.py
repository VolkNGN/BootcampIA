def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
    
def factorial(n):
    if n < 0:
        return "factorial is not defined for negative numbers"
    result = 1
    for i in range(1, int(n) + 1):
        result *= i
    return result    
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "6":
        print("Exiting Program.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", divide(num1, num2))
    elif choice == "5":
        num = float(input("Enter a number for factorial: "))
        if not num.is_integer():
            print("Factorial is only defined for integers.")
        else:
            print("Result: ", factorial(int(num)))

    else:
        print("Invalid choice. Please try again.")