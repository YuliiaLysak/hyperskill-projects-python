def intro():
    print("H A N G M A N")


def game():
    print("Guess the word:")
    word = input()
    if word == "python":
        print("You survived!")
    else:
        print("You lost!")


intro()
game()
