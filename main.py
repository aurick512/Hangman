import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

# Testing code
print("Welcome to hangman :)")
print(logo)
print("\n")

display = []
# Loops through the number of characters in a word, adds a "_" to the list "display" for every character
for _ in range(word_length):
    display += "_"

# Allows the user to guess multiple times until their lives run out
while not end_of_game:
    # Input user guess
    guess = input("Guess a letter: ").lower()
    clear()
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # Lets the user know that they've guessed the letter
        if letter == guess and guess in display:
            print(f"You've already guessed {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        # Reduces number of lives
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Used to print the hangman ASCII Art
    print(stages[lives])
