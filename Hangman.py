# importing a random variable
import random
name = input("What is your name? ")
# Here first enter the your name
print(name)
# A list of words 
words = ['rainbow', 'bolero', 'iqube', 'herohonda', 'electric', 'fassion', 'duo', 'activa', 'yamaha', 'h2r', 'suzuki', 'audi']
# Choose a random word from the list of words
word = random.choice(words)
print("Guess the character")
guesses = ""
# Number of turns used here
turns = 12
while turns > 0:
    # Counts the no.of times a user fails
    failed = 0
    # All characters from the input word taking one at a time.
    for char in word:
        # Comparing the character with in guesses
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            # Every failure 1 will be increamented with failure
            failed += 1

    if failed == 0:
        # You win will be given as output
        print("\nYou won!")
        # This print will give the correct word
        print("The word is:", word)
        break
    # If user has input the wrong word then it will ask the user to enter another word
    print()
    guess = input("Guess a character: ")
    # Every input character will be stored in guesses
    guesses += guess
    # Check the input with character in a word
    if guess not in word:
        turns -= 1
        # The character does not match the word then wrong will be given as a output
        print("Wrong")
        # This will print the number of turns left for the user
        print("You have", turns, "more guesses")
    if turns == 0:
        print("You lose!")