#Question1

fruits =["apple", "bannana", "grape", "pineapple"]

for fruits in fruits:
  print(fruits)

#Question2

count = 5 
while count >0:
  print(count)
  count -=1

#Question3

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for numbers in numbers:
  print(numbers)

#Question4

colors = ['black', 'blue', 'brown', 'pink', 'green', 'red']

import random

for color in range(3):
  random_color = random.choice(colors)
  print(random_color)