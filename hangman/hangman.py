import random

words = "python", "java", "swift", "javascript"


def intro():
    print("H A N G M A N")


def get_word_to_guess():
    return list(random.choice(words))


def show_guessed_letters(letter, word_to_guess, guessed):
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == letter:
            guessed[i] = letter

    return guessed


def play_game():
    word_to_guess = get_word_to_guess()
    guessed = ["-"] * len(word_to_guess)
    attempts = 8
    while attempts > 0:
        print()
        print("".join(guessed))
        print("Input a letter:")
        letter = input()
        attempts -= 1
        if letter in word_to_guess:
            guessed = show_guessed_letters(letter, word_to_guess, guessed)
        else:
            print("That letter doesn't appear in the word.")

    print("\nThanks for playing!")


intro()
play_game()
