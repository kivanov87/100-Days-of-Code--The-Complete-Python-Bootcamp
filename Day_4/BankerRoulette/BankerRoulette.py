names = names_string.split(", ")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
numItems = len(names)
randomChoice = random.randint(0, numItems - 1)
payer = names[randomChoice]

print(f"{payer} is going to buy the meal today!")