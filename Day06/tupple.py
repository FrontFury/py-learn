# Python Tuples — Complete Examples

# 1. Creating a Tuple (টাপল তৈরি করা)
empty_tuple = ()
empty_tuple_constructor = tuple()
print("Empty tuple:", empty_tuple)

# Single-item tuple (একটি আইটেমের টাপল তৈরি করতে অবশ্যই কমা দিতে হয়)
single_item = ("Python",)
print("Single item tuple:", single_item, "| Type:", type(single_item))

# Tuple with multiple items
fruits = ("banana", "orange", "mango", "lemon")
print("Fruits:", fruits)


# 2. Tuple Length (টাপলের দৈর্ঘ্য নির্ণয়)
print("Length of fruits tuple:", len(fruits))


# 3. Accessing Tuple Items (ইনডেক্সিংয়ের মাধ্যমে আইটেম অ্যাক্সেস)
# Positive Indexing (0 থেকে শুরু)
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit (positive index):", fruits[len(fruits) - 1])

# Negative Indexing (-1 থেকে শুরু)
print("Last fruit (negative index):", fruits[-1])
print("Second last fruit:", fruits[-2])


# 4. Slicing Tuples (টাপল স্লাইসিং)
print("All fruits [0:4]:", fruits[0:4])
print("Middle two fruits [1:3]:", fruits[1:3])
print("From index 1 to end [1:]:", fruits[1:])
print("Negative slice [-3:-1]:", fruits[-3:-1])


# 5. Changing / Modifying a Tuple (টাপলকে লিস্টে রূপান্তর করে পরিবর্তন)
# সরাসরি fruits[0] = "apple" লিখলে TypeError আসবে কারণ tuple immutable
fruits_list = list(fruits)
fruits_list[0] = "apple"
fruits_list.append("grape")
modified_fruits = tuple(fruits_list)
print("Modified tuple:", modified_fruits)


# 6. Checking an Item in a Tuple (আইটেম আছে কি না যাচাই)
print("Is 'orange' in fruits?", "orange" in fruits)
print("Is 'apple' in fruits?", "apple" in fruits)


# 7. Joining Tuples (দুই বা ততোধিক টাপল জোড়া লাগানো)
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
food_stuff = fruits + vegetables
print("Joined tuple (food_stuff):", food_stuff)


# 8. Tuple Methods: count() and index()
numbers = (10, 20, 30, 20, 40, 20, 50)
print("Count of 20:", numbers.count(20))
print("First index of 30:", numbers.index(30))


# 9. Unpacking a Tuple (টাপল আনপ্যাকিং)
person = ("Asabeneh", "Yetayeh", 250, "Finland")
first_name, last_name, age, country = person
print(f"Unpacked -> Name: {first_name} {last_name}, Age: {age}, Country: {country}")


# 10. Deleting a Tuple (সম্পূর্ণ টাপল ডিলিট করা)
temp_tuple = (1, 2, 3)
del temp_tuple
# print(temp_tuple)  # এটি আনকমেন্ট করলে NameError দেখাবে কারণ টাপলটি ডিলিট হয়ে গেছে
print("temp_tuple deleted successfully!")
