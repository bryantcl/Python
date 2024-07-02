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

import random

choices = ["rock", "paper", "scissors"]

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
userChoice = int(input())
if choices[userChoice] == "rock":
    print(rock)
elif choices[userChoice] == "paper":
    print(paper)
elif choices[userChoice] == "scissors":
    print(scissors)
print("\nComputer chose:\n")
compChoice = random.randint(0,2)
if choices[compChoice] == "rock":
    print(rock)
elif choices[compChoice] == "paper":
    print(paper)
elif choices[compChoice] == "scissors":
    print(scissors)
    
winMessage = "\nYou win!\n"
loseMessage = "\nYou lose!\n"
tieMessage = "\nTie!\n"

if userChoice == compChoice:
    print(tieMessage)

# Rock(0) wins against scissors(2)
# Scissors(2) wins agains paper(1)
# Paper(1) wins against rock(0)
elif userChoice == 0 and compChoice == 1:
    print(loseMessage)
elif userChoice == 0 and compChoice == 2:
    print(winMessage)
elif userChoice == 1 and compChoice == 2:
    print(loseMessage)
elif userChoice == 1 and compChoice == 0:
    print(winMessage)
elif userChoice == 2 and compChoice == 0:
    print(loseMessage)
elif userChoice == 2 and compChoice == 1:
    print(winMessage)
