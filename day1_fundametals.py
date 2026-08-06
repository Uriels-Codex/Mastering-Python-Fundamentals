# #task no.1
# name = "brent"
# age = 21
# height = 170.18
# isStudent = True

# print(name)
# print(age)
# print(height)
# print(f"Hello, my name is {name}. Currently {age} years old, with a height of {height}.\n" 
#       f"And if youre asking if I am a student??? The answer issssss...... {isStudent}")  

# print("\n\n")

# #Learn about F string and printing

# #task no.2

# print("Hello, please fill up the following info!")
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: ")) # type casting the input to int so the age will be a integer
# print(f"Your name is {user_name} and your age in 10 years is {user_age + 10}") # trying arithmetic expression

# print("\n\n")


#task no.3 
print("Check if Even or Odd.")
number = int(input("Enter a number: "))
if number %2 == 1 : #Always use a divisor after the modulus sign == 1 means 1 or more remainder 
    print("Odd")
else:
    print("Even")
print("\n")

#Type case to float to allow decimal and round them up for more accurate checking of grades...
#question: does it round up or round down automatically?
grade = float(input("Enter your grade: "))
if round(grade) >= 90:
    print("A")
elif round(grade) >= 80 :
    print("B")
elif round(grade) >= 70:
    print("C")
elif round(grade) >= 60:
    print("D")
else:
    print("F")