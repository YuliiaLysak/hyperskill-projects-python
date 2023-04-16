import random

words = "python", "java", "swift", "javascript"


def intro():
    print("H A N G M A N")


def game():
    word_to_guess = random.choice(words)
    print("Guess the word:")
    word = input()
    if word == word_to_guess:
        print("You survived!")
    else:
        print("You lost!")


intro()
game()
