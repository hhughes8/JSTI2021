import random

print("Let's play rock, paper, scissors!")

user_input = input("Rock, paper, or scissors?").lower()

WORDS = ("rock", "paper", "scissors")
word = random.choice(WORDS)
print ("Robot chose", random.choice(WORDS))

if random.choice(WORDS) == 'rock':
    if user_input == 'rock':
        print("Tied. Try again.")
    elif user_input == 'paper':
        print("User wins. Congrats!")
    elif user_input == 'scissors':
        print("You LOSE!")
    else:
        print("Invalid input. Valid inputs are: Rock, Paper, Scissors.")

if random.choice(WORDS) == 'paper':
    if user_input == 'paper':
        print("Tied. Try again.")
    elif user_input == 'scissors':
        print("User wins. Congrats!")
    elif user_input == 'rock':
        print("You LOSE!")
    else:
        print("Invalid input. Valid inputs are: Rock, Paper, Scissors.")

if random.choice(WORDS) == 'scissors':
    if user_input == 'scissors':
        print("Tied. Try again.")
    elif user_input == 'rock':
        print("User wins. Congrats!")
    elif user_input == 'paper':
        print("You LOSE!")
    else:
        print("Invalid input. Valid inputs are: Rock, Paper, Scissors.")
