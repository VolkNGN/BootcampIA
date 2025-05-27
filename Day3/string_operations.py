def reverse_string(s):
    reversed_string = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    cleaned_chars = []
    for c in s:
        if c.isalnum():
            cleaned_chars.append(c.lower())
    
    cleaned = ''
    for c in cleaned_chars:
        cleaned += c

    reversed_cleaned = ''
    for i in range(len(cleaned) - 1, -1, -1):
        reversed_cleaned += cleaned[i]
    
    return cleaned == reversed_cleaned
