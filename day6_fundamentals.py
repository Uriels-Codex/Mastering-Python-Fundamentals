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

remove_name = input("Enter the name you want to remove: ")

try:
    with open("profile.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: File nout found")

try:
    with open("profile.txt", "w") as file:
        for line in lines:
            if remove_name not in line:
                file.write(line)
except FileNotFoundError:
    print("Error: File nout found")

try:
    with open("profile.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error: File nout found")
    