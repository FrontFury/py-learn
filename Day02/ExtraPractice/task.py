# Day 2: 30 Days of python programming

import math

# ==========================================
# Exercises: Level 1
# ==========================================

first_name = "Asabeneh"
last_name = "Yetayeh"
full_name = first_name + " " + last_name
country = "Finland"
city = "Helsinki"
age = 250
year = 2026
is_married = True
is_true = True
is_light_on = False

# Declaring multiple variables on one line
language, framework, version, is_active = "Python", "Django", 3.15, True


# ==========================================
# Exercises: Level 2
# ==========================================

# 1. Check the data type of all variables using type()
print("--- Data Types ---")
print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("full_name:", type(full_name))
print("country:", type(country))
print("city:", type(city))
print("age:", type(age))
print("year:", type(year))
print("is_married:", type(is_married))
print("is_true:", type(is_true))
print("is_light_on:", type(is_light_on))
print("Multiple vars:", type(language), type(framework), type(version), type(is_active))

# 2. Find the length of your first name
print("\n--- Name Lengths ---")
print("Length of first_name:", len(first_name))

# 3. Compare the length of your first name and your last name
print("Length of last_name:", len(last_name))
print("Is first_name longer than last_name?", len(first_name) > len(last_name))
print("Difference in length:", abs(len(first_name) - len(last_name)))

# 4 - 11. Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("\n--- Arithmetic Results ---")
print("Total:", total)
print("Diff:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# 12. Circle calculations (radius = 30 meters)
radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

print("\n--- Circle Calculations (r = 30) ---")
print("Area of circle:", round(area_of_circle, 2))
print("Circumference of circle:", round(circum_of_circle, 2))

# 12.3. Take radius as user input and calculate the area
user_radius = float(input("\nEnter radius in meters: "))
user_area = math.pi * (user_radius ** 2)
print("Area for your radius:", round(user_area, 2))

# 13. Get user details using input()
print("\n--- User Input ---")
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

print(f"User: {user_first_name} {user_last_name}, Country: {user_country}, Age: {user_age}")

# 14. Check Python reserved words
print("\n--- Python Keywords ---")
help("keywords")