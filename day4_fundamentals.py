# import random
# day 4 of python fundamentals
#  ---review of day 3--without the bullets

# Exercise 1: Given actions = ["moved left", "picked up item", "opened door", "attacked enemy"], 
# pop the last action off, store it in a variable, print f"Undoing: {last_action}", 
# then print the remaining list to confirm it's gone.

# actions = ["moved left", "picked up item", "opened door", "attacked enemy"]
# last_actions= actions.pop(-1)
# print(f"Undoing: {last_actions}")
# print(actions)

# Exercise 2: Given deck = ["A", "K", "Q", "J", "10", "9"] 
# (remember to import random), use random.randint() with correct off-by-one math to generate a valid random 
# index, pop that card out and store it, then print what was drawn along with the remaining deck.

# deck = ["A", "K", "Q", "J", "10", "9"]
# card_drawn = deck.pop(random.randint(0, len(deck)- 1))
# print(card_drawn)
# print(f"remaining deck: {deck}")

# Exercise 3: Given inventory = ["sword", "shield", "potion", "expired_scroll"], use .remove() 
# to get rid of "expired_scroll" by name (no need to capture a return value here), then print the final 
# inventory.

# inventory = ["sword", "shield", "potion", "expired_scroll"]
# inventory.remove("expired_scroll")
# print(inventory)

# --Dictionaries--
# Task 1: Basic dictionary operations
# Create a dictionary representing yourself with at least 4 keys (name, age, favorite game, whatever you want). 
# Then:
# Print one value using its key
# Add a new key-value pair
# Update an existing value
# Delete one key-value pair
# Print the final dictionary

# about_me = {
#     "name" : "UrieL Akiraa",
#     "age" : 21,
#     "favorite_game" : "Valorant",
#     "Hobbie/s" : "Coding"
# }
# print(f"The name is {about_me["name"]}")
# about_me["Gay friend"] = "Miles Santos"
# about_me["age"] = 100000
# del about_me["Hobbie/s"]
# print(f"here is the final output for the dictionary, {about_me}")

# task 2  looping over items

# student_grade = {
#     "Brent" : 100,
#     "Rita": 100,
#     "Mei" : 90,
#     "Kiana" : 30,
#     "Bronya" : 50
# }
# total_grade = 0
# for name ,grades in student_grade.items():
#     print(f"{name}, Grade is = {grades}")
#     total_grade += grades
# class_average = total_grade / len(student_grade)
# print(f"the class average grade is: {class_average}")

#Task 3: Building a dictionary from scratch, dynamically

# user_dict = {}
# key1 = input("Enter key: ")
# val1 = input("Enter val: ")
# user_dict[key1] = val1
# key2 = input("Enter key: ")
# val2 = input("Enter val: ")
# user_dict[key2] = val2
# key3 = input("Enter key: ")
# val3 = input("Enter val: ")
# user_dict[key3] = val3
#----------------different solution----------
# for index in range(3):
#     index += 1
#     kay = input("Enter the key: ")
#     vals = input("Enter the val: ")
#     user_dict[kay] = vals
# for ky, val in user_dict.items():
#     print(f"key = {ky} :  val= {val}")

# print(f"the total value of the dictionary is: {len(user_dict)}")
# user_dict = {}
# while True:
#     kay = input("Enter the key: ")
#     val = input("Enter the val: ")
#     if kay.lower() == "stop" or val.lower() == "stop":
#         break
#     user_dict[kay] = val
# print("Here are the items of user dictionary")
# for name, val in user_dict.items():
#     print(f"{name} : {val}")
# print(f"User Dictionay item count: {len(user_dict)}")

#Topic 2, functions
# Task 1: Basic function with a return value
# Write a function called calculate_area that takes width and height as parameters,
#  and returns the area (width × height) — don't print inside the function, just 
#  return the value. Then call it with a few different numbers and print the results 
#  outside the function.

# def calculate_area (width, height):
#     return width * height
# res1 = calculate_area(1, 2)
# res2 = calculate_area(121, 23)
# res3 = calculate_area(11, 24)
# print(f"here are the result: {res1} \n {res2} \n {res3}")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

#task 2
# def get_min_max(numbers):
#     return max(numbers), min(numbers)
# def print_min_max(number_list):
#     max_val, min_val = get_min_max(number_list)
#     print(f"Largest: {max_val}, Smalles: {min_val}")
# def main_menu():
#     num_list = []
#     print("Write 0 if want to stop")
#     while True:
#         num = int(input("Enter a num: "))
#         if num == 0:
#             break
#         num_list.append(num)
#     print_min_max(num_list)
# main_menu()

#task3 Default arguments

# def describe_pet(name, animal_type = "dog"):
#     print(f"my pet which is a {animal_type}, name is {name}")
# def main():
#     describe_pet("Frieren", "Cat")
#     describe_pet("Sizu")
# main()

# Task 4: *args — variable number of arguments
# def add_all(*numbers):
#     total = 0
#     for i in numbers:
#         total+= i
#     return total

# print(add_all(10,20))
# print(add_all(10,20, 30, 40, 50))