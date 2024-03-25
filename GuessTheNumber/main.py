from replit import clear
from ascii import logo
import random

random_num = random.randint(1,100)
NO_LIVES ="You run out of guesses, you lose"
LOGO = logo

def easy():
    print(LOGO)
    random_num = random.randint(1, 100)
    lives = 10
    print(f"You have {lives} attempts remaining to guess the numebr")
    game_end = False
    while not game_end:
        user_num = int(input("Make a guess: "))
        if user_num > random_num:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the numebr")
            if lives == 0:
                print(NO_LIVES)
                clear()
                return False
            print("Too high\nGuess again")

        elif user_num < random_num:
            lives-= 1
            print(f"You have {lives} attempts remaining to guess the numebr")
            if lives == 0:
                print(NO_LIVES)
                clear()
                return False
            print("Too low\nGuess again")
        else:
            print(f"You win! the number is {random_num}")
            print(f"You survived with {lives} attempts remaining to guess the numebr")
            game_end = True

def hard():
    print(LOGO)
    random_num = random.randint(1, 100)
    lives = 5
    print(f"You have {lives} attempts remaining to guess the numebr")
    game_end = False
    while not game_end:
        user_num = int(input("Make a guess: "))
        if user_num > random_num:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the numebr")
            if lives == 0:
                print(NO_LIVES)
                game_end = True
                clear()
                return False
            print("Too high\n.Guess again")

        elif user_num < random_num:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the numebr")
            if lives == 0:
                print(NO_LIVES)
                game_end = True
            print("Too low\nGuess again")
        else:
            print(f"You win! the number is {random_num}")
            print(f"You survived with {lives} attempts remaining to guess the numebr")
            game_end = True

stop_play = False
while not stop_play:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' to guess the number. ")
    if difficulty == 'easy':
        easy()
    elif difficulty == 'hard':
        hard()



