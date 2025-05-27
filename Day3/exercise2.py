import math_operations as mo
import string_operations as so

num1 = 10
num2 = 5
text = "Kayak"

print("Original:", text)
print("Reversed:", so.reverse_string(text))
print("Number of vowels:", so.count_vowels(text))
print("Is palindrome?:", so.is_palindrome(text))

print("Addition: ", mo.add(num1, num2))
print("Subtraction: ", mo.subtract(num1, num2))
print("Multiplication: ", mo.multiply(num1, num2))
print("Division: ", mo.divide(num1, num2))