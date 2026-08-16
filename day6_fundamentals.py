#TOPIC TODAY: File input and output

# Task 1: Write a program that asks the user for their name and favorite game 
# then writes both to a file called profile.txt, each on its own line, using with 
# open(...) as f: in write mode. Afterward, open the file separately in read mode 
# wrapped in try/except for FileNotFoundError, just in case), and print its full 
# contents back out to confirm it saved correctly.
# Try it, paste your code when ready.

# name = input("Enter the your name: ") # ---> im reusing this for editing text(removing) so write is in comment  
# game = input("Enter your game: ") # ---> im reusing this for append so write is in comment  

# with open("profile.txt", "w") as f: --> creating and writting in file
#     f.write(f"My name is {name} \n")
#     f.write(f"and my fav game is: {game}")


# try:
#     with open("profile.txt", "r") as file: -->reading file
#         contents = file.read()
#         print(contents)
# except FileNotFoundError:
#     print("Erorr: File not found or dont exist")

# with open("profile.txt", "a") as file: ----> adding new lines on the existing file
#     file.write("New User:\n")
#     file.write(f"Name: {name}, favorite game: {game}")

# with open("profile.txt", "r") as file: --> reading line by line to check if it saved
#     for line in file:
#         print(line)

# remove_name = input("Enter the name you want to remove: ")

# try:
#     with open("profile.txt", "r") as file:
#         lines = file.readlines()
# except FileNotFoundError:
#     print("Error: File nout found")

# try:
#     with open("profile.txt", "w") as file:
#         for line in lines:
#             if remove_name not in line:
#                 file.write(line)
# except FileNotFoundError:
#     print("Error: File nout found")

# try:
#     with open("profile.txt", "r") as file:
#         for line in file:
#             print(line)
# except FileNotFoundError:
#     print("Error: File nout found")

# Exercise 1
# You have a file called notes.txt with several lines of text. 
# Write a program that reads the file, and prints only the lines that contain 
# a specific word the user types in.
# Go ahead.

# with open("notes.txt", "w") as note:
#     note.write("Brent yuri chavez \n")
#     note.write("Kairo Santillan \n")
#     note.write("Jamir Eric Santos \n")
#     note.write("Julian Sampang \n")
#     note.write("David Elie Dela Peña \n")
#     note.write("Joseph Miles Santos \n")
#     note.write("Kent Andrew Pecson \n")
#     note.write("Ralph Vincent Yuzon \n")

# try:
#     with open("notes.txt", "r") as note:
#         for line in note:
#             if "J" in line:
#                 print(line)
# except FileNotFoundError:
#     print("Error")

#Exercise 2
# total_words = 0
# whole_total = 0
# try:
#     with open("generated files/notes.txt", "r") as notes:
#         for line in notes:
#             total_words = line.split()
#             whole_total += len(total_words)
#             print(f"Total word for this line is {len(total_words)}")
#         print(f"the total word is: {whole_total}")
# except FileNotFoundError:
#     print("Error file not found")


# Exercise 3
# Using the same notes.txt file, write a program that reads the file, 
# and instead of just printing matching lines, counts how many lines contain a 
# specific word the user types in — then prints just the total count at the end 
# (not the lines themselves).
# Go ahead.

# total = 0
# try:
#     with open("generated files/notes.txt", "r") as notes:
#         user_input = input("Enter a word: ")
#         for line in notes:
#             if user_input in line:
#                 total += line.count(user_input)
#         print(f"The total line of where the word {user_input} is in us: {total}")
# except FileNotFoundError:
#     print("Error File not Fouund")

# Same notes.txt file — write a program that asks the user for a word, then writes only 
# the matching lines (the ones containing that word) into a brand new file called 
# matches.txt, instead of just counting or printing them.
# Go ahead.

user_input = input("Enter a word: ")
split_content = user_input.split()
match_content = []
# print(f"split content items: {split_content}") #--> Use to check if the words were split and for mental model for debugging
try:
    with open("generated files/notes.txt", "r") as notes:
        for line in notes: 
            for words in split_content:
                if words in line:
                    match_content.append(line)
                    break
    #----> I use it to check the current state/items of the list if it stored the lines
    # for words in match_content: 
    #     print(f" items in match content list: {words}")
    with open ("matches.txt", "w") as matchtext:
        for match in match_content:
            matchtext.write(match)
except FileNotFoundError:
    print("Error File not found")