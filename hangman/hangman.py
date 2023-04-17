import random

words = "python", "java", "swift", "javascript"
input_letters = []


def intro():
    print("H A N G M A N")


def get_word_to_guess():
    return list(random.choice(words))


def validate_input(user_input):
    if len(user_input) != 1:
        print("Please, input a single letter.")
        return False
    elif not user_input.isalpha() or user_input.isupper():
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    elif user_input in input_letters:
        print("You've already guessed this letter.")
        return False
    else:
        input_letters.append(user_input)
        return True


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
        result = "".join(guessed)
        print()
        print(f"You guessed the word {result}!")
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
        if not validate_input(letter):
            continue
        elif letter in word_to_guess:
            guessed = show_guessed_letters(letter, word_to_guess, guessed)
            if "-" not in guessed:
                break
        else:
            allowed_mistakes -= 1
            print(f"That letter doesn't appear in the word.  # {allowed_mistakes} attempts")

    evaluate_result(guessed)


intro()
play_game()
