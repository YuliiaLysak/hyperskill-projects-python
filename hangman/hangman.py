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


def evaluate_result(guessed):
    if "-" in guessed:
        print()
        print("You lost!")
    else:
        print()
        print("".join(guessed))
        print("You guessed the word!")
        print("You survived!")


def play_game():
    word_to_guess = get_word_to_guess()
    guessed = ["-"] * len(word_to_guess)
    allowed_mistakes = 8
    while allowed_mistakes > 0:
        print()
        print("".join(guessed))
        print("Input a letter:")
        letter = input()
        if letter in guessed:
            print("No improvements.")
            allowed_mistakes -= 1
        elif letter in word_to_guess:
            guessed = show_guessed_letters(letter, word_to_guess, guessed)
            if "-" not in guessed:
                break
        else:
            print("That letter doesn't appear in the word.")
            allowed_mistakes -= 1

    evaluate_result(guessed)


intro()
play_game()
