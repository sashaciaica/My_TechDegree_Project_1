from random import randint
ran_num = randint(1, 10)  # Pick a random number between 1 and 10.

def start_game():
    guess = int(input("Welcome: Please type a random number 1-10: "))
    guesses = 1
    while guess != ran_num:
        if guess > ran_num:
            print("Your guess is too high")
            guess = int(input("Welcome: Please type a random number 1-10: "))
            guesses = guesses + 1
        elif guess < ran_num:
            print("Your guess is too low")
            guess = int(input("Welcome: Please type a random number 1-10: "))
            guesses = guesses + 1
    
    print("Success")
    print("It took you ", guesses, "of guesses")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
