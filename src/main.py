import random


def get_integer_input(prompt, lower_bound=None, upper_bound=None, previous_guesses=None):
    """
    Requests input from the user and only accepts an integer within the specified range.
    If the number has been guessed before, it prompts again without counting as an attempt.

    :param prompt: str
    :param lower_bound: int or None
    :param upper_bound: int or None
    :param previous_guesses: set or None
    :return: int
    """
    while True:
        try:
            guess = int(input(prompt))
            if (lower_bound is not None and guess < lower_bound) or (upper_bound is not None and guess > upper_bound):
                print(
                    f"Die Zahl liegt außerhalb des Bereichs von {lower_bound} bis {upper_bound}. Bitte versuchen Sie es erneut.")
            elif previous_guesses is not None and guess in previous_guesses:
                print("Sie haben diese Zahl bereits geraten. Bitte versuchen Sie es mit einer anderen Zahl.")
            else:
                return guess
        except ValueError:
            print("Das ist keine gültige Zahl. Bitte versuchen Sie es erneut.")


def guessing_game():
    """
    Runs the guessing game where the user has to guess a randomly generated number
    within a range they specify. The user has 3 attempts and the guess must be within the range.
    Repeated guesses do not count as an attempt.
    """
    print("Willkommen zum Ratespiel!")

    lower_bound = get_integer_input("Bitte geben Sie die untere Grenze des Bereichs ein: ")
    upper_bound = get_integer_input("Bitte geben Sie die obere Grenze des Bereichs ein: ")

    random_number = random.randint(lower_bound, upper_bound)
    attempts = 3
    previous_guesses = set()

    print(
        f"Sie haben {attempts} Versuche, um die Zahl zu erraten. Die Zahl liegt zwischen {lower_bound} und {upper_bound}.")

    while attempts > 0:
        guess = get_integer_input("Bitte geben Sie Ihre Vermutung ein: ", lower_bound, upper_bound, previous_guesses)

        if guess == random_number:
            print("Herzlichen Glückwunsch! Sie haben die Zahl richtig erraten.")
            break
        else:
            previous_guesses.add(guess)
            attempts -= 1
            if attempts > 0:
                print(f"Das ist nicht korrekt. {attempts} Versuch(e) verbleiben.")
            else:
                print(f"Leider haben Sie alle Versuche verbraucht. Die richtige Zahl war {random_number}.")


if __name__ == "__main__":
    guessing_game()
