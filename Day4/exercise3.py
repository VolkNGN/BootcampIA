my_list = [1, 2, 3, 2, 4, 1, 5]

# Remove duplicates using a set
unique_list = list(set(my_list))

# Reverse the list
unique_list.reverse()

print(unique_list)

grades = {
    "Alice": 25,
    "Sidney": 31,
    "Nadine": 32,
    "Xavier": 35
}

# Calculate the average grade
average = sum(grades.values()) / len(grades)

print(f"Average grade: {average:.2f}")
