import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
completed = False
hangman = 0
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = []
for space in range(0, len(chosen_word)):
    display.append("_")
print(display)    
while completed == False:
    guess = input("Guess a letter: ").lower()
    for letter in range(0, len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess
    print(display)
    if (list(chosen_word) == display):
        completed = True
    else:
        hangman = hangman + 1
        if hangman == 10:
            completed = True

if hangman == 10:
    print("Hangman, you lose!")
elif hangman < 10:
    print("You win!")
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.