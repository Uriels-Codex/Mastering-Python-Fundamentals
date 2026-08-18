#Topic, Tuples

# student = ("Uriel", 21 , "BSCS")

# name, age, course =  student
# print(f"THe name is {name}, age is {age}, and their coursei s {course}")
# student[1] = 22

# Got it — task only, no code, no hints:
# Loop through the students list of tuples, unpack each tuple into two variables per 
# iteration, and print each student with their course.
# Separately, figure out how to count how many students are taking "BSCS" — 
# try using .count() first, see what happens, and be ready to explain why it does or 
# doesn't work the way you expect.

students = [("Uriel", 1), ("Jamir", "BSIT"), ("David", "BSIT")]
for name, course in students:
    print(f"Name:{name}, course is: {course}")
print(f"Total count of BSCS course: {students.count("BSIT")}")
print(students.count(1))

# numbers = (23, 23, 23, 23,12 ,235,12,4,5,1)
numbers = [(23, 23), (23, 23), (12 ,235),(12,4),(5,1)]

print(numbers.count(23))