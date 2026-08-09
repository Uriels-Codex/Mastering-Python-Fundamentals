# day 3 of learning python fundamentals
#review

# fooc_count = 0
# print("Type STOP, if u want to stop..")
# while (True) :
#     fav_food = input("Enter your favourite food: ")
#     if fav_food == "" or not fav_food:
#         print("Please type something....")
#     elif fav_food == "Stop" or fav_food == "stop" or fav_food == "STOP":
#         break
#     else:
#         fooc_count +=1

# print(f"the total number of food you entered is {fooc_count}")

# task no2
# numbers = [10,221,1,2,4,12,656,67,3,1,0]

# for n in numbers:
#     if n > 10:
#         print(n)

#task no3
# for row in range(1, 5):
#     for number in range(row):
#         print(number + 1, end="")
#     print("")

#TOPIC for day 3 -----> LIST
# task no.1
# Make a list of 5 of your favorite anime/shows/movies
# Print the whole list
# Print just the first and last item using indexing
# Add one more item using .append()
# Remove one item using .remove()
# Print the final list and its length using len()

# fav_shows = ["Steins Gate", "Seishun Buta Yarou", "Persona", "Final Fantasy", "Nijisanji"]
# for index, shows in enumerate(fav_shows):
#     index += 1
#     print(f"{index}. {shows}")
# print (f"The first item is {fav_shows[0]}, And the last item is {fav_shows[-1]}")
# fav_shows.append("Noragami")
# fav_shows.remove("Nijisanji")
# print(f"The last item of the list is {fav_shows[-1]}, and the number of item is {len(fav_shows)}")
# print("Nijisanji" in fav_shows)


# Task 2: Sorting and searching
# Make a list of 6-8 random numbers (not in order)
# Print the original list
# Sort it in ascending order using .sort(), print it
# Sort it in descending order (hint: .sort(reverse=True)), print it
# Find the largest and smallest number using max() and min() — no manual loop needed, these are built-in functions
# Check if a specific number exists in the list using in, and print the result

# numbers = [1,12,43,65,8,7,23,1,2,5]

# for n in numbers: # normal print
#     print(n)
# print("---------------")
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True) # --> by this point the og list ir already in reverse
# print(numbers)
# print(f"The largest number is {max(numbers)}, while the smallest is {min(numbers)}")
# print(21 in numbers)


# Task 3: Filtering into a new list
# Make a list of 8-10 numbers
# Loop through and build a new list containing only numbers greater than 20
# Print both the original and the new filtered list

numbers = [1,12,43,65,8,7,23,1,2,5]
new_numList = []
for n in numbers:
    if n > 20:
        new_numList.append(n)

print(numbers)
print(new_numList)