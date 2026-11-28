# Python Sets — Complete Examples

# 1. Creating a Set (সেট তৈরি করা)
empty_set = set()  # ফাঁকা সেট তৈরি করতে অবশ্যই set() ব্যবহার করতে হয় ({} দিলে dictionary হয়)
print("Empty set:", empty_set, "| Type:", type(empty_set))

fruits = {"banana", "orange", "mango", "lemon"}
print("Fruits set:", fruits)


# 2. Set Length & Accessing Items (সেটের দৈর্ঘ্য নির্ণয় ও লুপ দিয়ে অ্যাক্সেস)
print("Length of fruits set:", len(fruits))

print("Looping through fruits:")
for fruit in fruits:
    print(" -", fruit)


# 3. Checking an Item in a Set (আইটেম আছে কি না যাচাই)
print("Is 'mango' in fruits?", "mango" in fruits)
print("Is 'apple' in fruits?", "apple" in fruits)


# 4. Adding Items to a Set (নতুন আইটেম যোগ করা: add ও update)
# একটি আইটেম যোগ করতে add()
fruits.add("lime")
print("After add('lime'):", fruits)

# একাধিক আইটেম যোগ করতে update()
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)
print("After update(vegetables):", fruits)


# 5. Removing Items from a Set (আইটেম মুছে ফেলা: remove, discard, pop, clear)
items = {"item1", "item2", "item3", "item4"}
items.remove("item2")     # আইটেম না থাকলে KeyError দেখাবে
items.discard("item99")   # আইটেম না থাকলেও কোনো Error দেখাবে না
print("After remove & discard:", items)

removed_item = items.pop()  # যেকোনো একটি র‍্যান্ডম আইটেম মুছে রিটার্ন করে
print("Popped item:", removed_item, "| Remaining:", items)

items.clear()  # সেটের সব আইটেম মুছে ফাঁকা করে দেয়
print("After clear():", items)


# 6. Converting List to Set (লিস্ট থেকে সেটে রূপান্তর করে ডুপ্লিকেট বাদ দেওয়া)
numbers_list = [10, 20, 30, 20, 40, 10, 50]
unique_numbers = set(numbers_list)
print("Original list:", numbers_list)
print("Unique set:", unique_numbers)


# 7. Joining Sets (দুটি সেট জোড়া লাগানো: union বা |)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)  # অথবা: set_a | set_b
print("Union (set_a | set_b):", union_set)


# 8. Finding Intersection Items (কমন উপাদান নির্ণয়: intersection বা &)
intersection_set = set_a.intersection(set_b)  # অথবা: set_a & set_b
print("Intersection (set_a & set_b):", intersection_set)


# 9. Difference & Symmetric Difference (- এবং ^)
print("Difference (set_a - set_b):", set_a.difference(set_b))
print("Difference (set_b - set_a):", set_b - set_a)
print("Symmetric Difference (set_a ^ set_b):", set_a.symmetric_difference(set_b))


# 10. Subset, Superset & Disjoint Sets (issubset, issuperset, isdisjoint)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}

print("Is even_numbers subset of whole_numbers?", even_numbers.issubset(whole_numbers))
print("Is whole_numbers superset of even_numbers?", whole_numbers.issuperset(even_numbers))
print("Are even and odd disjoint sets?", even_numbers.isdisjoint(odd_numbers))


# 11. Deleting a Set (সম্পূর্ণ সেট ডিলিট করা)
temp_set = {"a", "b", "c"}
del temp_set
# print(temp_set)  # এটি আনকমেন্ট করলে NameError দেখাবে কারণ সেটটি ডিলিট হয়ে গেছে
print("temp_set deleted successfully!")
