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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
comp_input = random.randint(0, 2)
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
if comp_input == 0:
    print(rock)
elif comp_input == 1:
    print(paper)
elif comp_input == 2:
    print(scissors)
if user_input == comp_input:
    print("Its a tie")
else:
    if user_input - comp_input == 1:
        print("You win")

    else:
        print("You lose")