from random import randint
ran_num = randint(1, 10)  # Pick a random number between 1 and 10.

def start_game():
    try:
        guess = int(input("Welcome: Please type a random number between 1 and 10 "))
        guesses = 1

        if guess in range(1,10):
            breakpoint()
        elif guess < 0:
            raise ZeroDivisionError
        else:
            print("Out of range")

        while guess != ran_num:
            if guess > ran_num:
                print("Your guess is too high")
                guess = int(input("Welcome: Please type a random number between 1 and 10 "))
                guesses = guesses + 1
            elif guess < ran_num:
                print("Your guess is too low")
                guess = int(input("Welcome: Please type a random number between 1 and 10 "))
                guesses = guesses + 1
    except ZeroDivisionError:
        print("Ups. Bellow zero value. Try again")
    except:
        print("No way. I said a number not a string")
    else:
        print("Success")
        print("It took you ", guesses, "of guesses")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
