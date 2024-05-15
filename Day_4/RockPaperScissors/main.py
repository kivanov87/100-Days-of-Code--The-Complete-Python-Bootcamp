rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
gameImages = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(gameImages[user_choice])
aiChoice = random.randint(0,2)
print(f"Computer chose:")
print(gameImages[aiChoice])

if user_choice>=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and aiChoice == 2:
    print("You win!")
elif user_choice == 2 and aiChoice == 0:
    print("You lose")
elif user_choice > aiChoice:
    print("You win!")
elif user_choice < aiChoice:
    print("You lose")
elif user_choice == aiChoice:
    print("Drawwww")


