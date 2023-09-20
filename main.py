#Task 1

import random
dice_roll = int(input("How many dice do you want to roll"))

total_rolls = 0

for i in range (dice_roll):
    roll = random.randint(1,6)
    total_rolls += roll
    print(roll)
print(f"the sum of the {dice_roll} dices rolled is {total_rolls}")


#Task 2
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    if user_input.replace(".", "", 1).isdigit() or (
            user_input[0] == '-' and user_input[1:].replace(".", "", 1).isdigit()):
        number = float(user_input)
        numbers.append(number)
    else:
        print("Invalid input. Please enter a valid number.")

if len(numbers) >= 5:
    numbers.sort(reverse=True)
    top_five = numbers[:5]

    print("The five greatest numbers in descending order are:")
    for i, num in enumerate(top_five, start=1):
        print(f"{i}. {num}")
else:
    print("You entered fewer than five numbers.")

#Task 3
import math

user_input = int(input("Enter an integer"))

for i in range(2,user_input):
    if user_input % i == 0:
        print(f"{user_input} is not a prime number")
        break
else:
    print(f"{user_input} is a prime number")

#Task 4
cities = []
for i in range(5):
    city_name = input(f"enter the name of a city {i +1}: ")
    cities.append(city_name)

print("Cities entered:")
for city in cities:
    print(city)


