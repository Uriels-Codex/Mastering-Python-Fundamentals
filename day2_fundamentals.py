# # # games = ["Valorant", "Mobile Legends", "Dota2"]
# # # print("This are the games that I love playing: ")
# # # for index, game in enumerate(games):
# # #     index += 1
# # #     print(index, game)

# # # # for letter in "Brent":
# # # #     print(letter)


# # numbers = [22, 21, 54, 34 , 66, 67 , 21, 1]
# # even_num = []
# # for n in numbers:
# #     if n %2 == 0:
# #         even_num.append(n)
# # print(even_num)

# # #task 1: Print Hello 3 times using range
# # for i in range(3):
# #     print("Hello")

# # # Exercise 2: Make a list of 3 of your favorite games, 
# # # loop through it, print "I like playing {game}" for each
# # games = ["Valorant", "Dota2", "Mobile Legends"]
# # for game in games:
# #     print("I like playing ", game)

# # # Exercise 3: Loop over your own name, print each letter on its own line
# # name = "Brent"
# # for letter in name:
# #     print(letter)

# # # Exercise 4: Loop over your favorite-games list again,
# # # but print numbered like "1. Game Name", "2. Game Name"
# # games = ["Valo", "MonHun", "FF7"]
# # for index, game in enumerate(games):
# #     index += 1
# #     print(index,". ", game)

# #Exercise no5, create new list from 1-10 and only add the even number then print new list
# # num = [1,2,3,4,5,6,7,8,9,10]
# # even_total = []
# # for n in num:
# #     if n %2 == 0:
# #         even_total.append(n)
# # print(even_total)

# # Bonus Exercise 6: Loop through numbers 1-20, skip printing any number divisible by 3
# # for i in range(1, 21):
# #     if i %3 == 0:
# #         continue
# #     else:
# #         print(i)

# #Fizzbuzz challenge
# # fizz_count = 0
# # fizzbuz_count = 0
# # buzz_count = 0
# # for i in range(1, 31):
# #     if i %3 == 0 and i %5 == 0:
# #         print("FizzBuzz")
# #         fizzbuz_count += 1
# #     elif i %3 == 0:
# #         print("Fizz")
# #         fizz_count +=1
# #     elif i %5 == 0:
# #         print("Buzz")
# #         buzz_count += 1
# #     else:
# #         print(i)
# # print(f"\nFIzzBuzz count {fizzbuz_count}")
# # print(f"FIzz count {fizz_count}")
# # print(f"Buzz count {buzz_count}")

# #looping once and adding all the numbers > 5 and counting the total numbers
# #numbers = [4, 7, 2, 9, 3, 10, 6, 1, 8, 5]
# greaterThanfive_counter = 0
# total = 0
# for num in numbers:
#     if num > 5:
#         greaterThanfive_counter += 1
#         total += num
# print(f"Count: {greaterThanfive_counter}, Sum: {total}")  

# for row in range(1, 6):
#     for star in range(row):
#         print("*", end="")
#     print()

# #explanation as to why it reversed... the second loop is always dependent into the first
# which is the row. If row is 1 then star is 1 and so is the * that will print.. reverse that
# if the row is at 5 then the star is 5 and so the number of * will be print. in order to
# achieve this, I use the start, stop and step argument of the range function where as the first
# argument will always be the starting point and is inclusive, 2nd argument which is the 
# desired stop of the count that needs to have extra one count since its exlusive, and
# lastly the third argument decide on how much will the count be, so -1 is literally
# minus/subtracting one to the 1st argument to reach the 2nd argument

# for row in range(5, 0, -1):
#     for star in range(row):
#         print("*", end="")
#     print()

