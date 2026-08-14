#day 5 error handling (try/except)
# Task 1: Write a program that asks the user to enter a number, 
# then divides 100 by it. Wrap the risky part in try/except, catching 
# ValueError (if they type something that isn't a number) and ZeroDivisionError 
# (if they enter 0) as separate except blocks, each with its own friendly error message.

# try:
#     num = int(input("Enter a num: "))       
#     result = 100 / num
# except ValueError:
#     print("Please make sure that what you entered is a number!")
# except ZeroDivisionError:
#     print("Please put a number aside from 0 !!")

# Task 2: Handling IndexError and KeyError
# Create a list of 3 favorite games, and ask the user to enter an index number 
# (like 0, 1, 2...) to pick one. Use try/except to catch IndexError in case they enter a 
# number outside the list's range (like 5), printing a friendly message instead of crashing.
# Then, separately: create a small dictionary of 3 people and their ages. Ask the user to 
# enter a name, and try to print that person's age. Catch KeyError in case they enter a
# 'name that isn't in the dictionary.

# fav_games = ["Valorant", "Final fantasy", "Persona 3"]

# try:
#     num = int(input("Enter desired index to access a game: "))
#     print(f"The game that you cose is:  {fav_games[num - 1]}")
# except IndexError:
#     print("Error: chosen index doesnt exist!!")

# initially I put the print message for the succeess run on else, but when I try
# putting a wrong index, the exception message is not being trigger, python default message
# pop up. So I put the print message on try, if no error then itll just print.. 
#still need to properly know when to use else and finally

# user_details = {}
# for i in range(3):
#     ky = input("Enter a keyword: ")
#     val = input("Enter a value: ")

#     try:
#         val = int(val)
#     except ValueError:
#         try:
#             val = float(val)
#         except ValueError:
#             pass 
#     user_details[ky] = val
# try:
#     name = input("Enter a name: ")
#     print(f"{name} age is {user_details[name]}")
# except KeyError:
#     print("Error: key doesn't exist")


# attempting to practice nesteed try - catch/execept and converting if ValueError

# inven_items ={}

# for i in range(4):
#     try:
#         item_name = input("Enter the item name: ")
#     except ValueError:
#         print("Please enter a proper word for the item name...")

#     item_stocks = input("Enter the quantity: ") # better to parse it already in int but for practice
#     for convert in [int, float]:
#         try:
#             item_stocks = convert(item_stocks)
#             break
#         except ValueError:
#             continue
#     inven_items[item_name] = item_stocks

# for item, quantity in inven_items.items():
#     print(f"Item= {item} : Quantity= {quantity} {type(quantity)}")

# one last try on retry logic since I think Im still weak at error handling

# while True:
#     try:
#         num1 = int(input("Enter a number 1: "))
#         break
#     except ValueError:
#         print("Error: input is not integer")

# while True:
#     try:
#         num2 = int(input("Enter a number 2: "))
#         break
#     except ValueError:
#         print("Error: input is not integer")

# while True:
#     try:
#         num3 = int(input("Enter a number 3: "))
#         break
#     except ValueError:
#         print("Error: input is not integer")
        
# I thought that its too repetitive so I tried cleaning it a bit using loops
# num_list = []

# for i in range(3):
#     while True:
#         try:
#             num = int(input(f"Enter number {i+1}: "))
#             num_list.append(num)
#             break
#         except ValueError:
#             print("Error: Input must be whole number")
# print("This are the item in the list: ")
# for nums in num_list:
#     print(nums)