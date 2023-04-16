import random

words = "python", "java", "swift", "javascript"


def intro():
    print("H A N G M A N")


def get_word_to_guess():
    return random.choice(words)


def replace_with_hyphens(word):
    hyphens_count = len(word) - 3
    return word[0:3] + "-" * hyphens_count


def game():
    word_to_guess = get_word_to_guess()
    word_to_show = replace_with_hyphens(word_to_guess)
    print("Guess the word: " + word_to_show)
    word = input()
    if word == word_to_guess:
        print("You survived!")
    else:
        print("You lost!")


intro()
game()
