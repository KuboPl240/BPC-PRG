import random

GAME_SYMBOLS = ["rock", "paper", "scissors"]


def play_rock_paper_scissor(user_name, user_choice):
    """
    Return winner of the game Rock, paper, scissor.
    :param str user_name: name of the player
    :param str user_choice: symbol of the player
    :rtype: str
    :return: vitez hry kamen, nuzky, papir - "Tie", "computer" or user_name
    """
    # Nahodny vyber cisla (0, 1 nebo 2), ktere urcuje tah pocitace
    computer_choice_idx = random.randint(0, 2)

    # Podle vybraneho cisla (indexu), vyberte odpovidajici textovy retezec z konstanty GAME_SYMBOLS
    computer_choice = GAME_SYMBOLS[computer_choice_idx]

    # Zmente prvni pismeno retezce jmena hrace na velke pismeno
    user_name = user_name.capitalize()

    # Zmente retezec s tahem hrace na mala pismena
    user_choice = user_choice.lower()

    # Doplnte podminku: tah hrace neni mezi symboly, ktere muze pouzit pocitac
    if user_choice not in GAME_SYMBOLS:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
        return None

    # Hra kamen, nuzky, papir
    # Shoda tahu
    if user_choice == computer_choice:
        print("It's a tie!")
        return "Tie"
    # Doplnte zbylou cast hry podle pravidel (viz README)


    # Nasledujici dvojice radku podle potreby vlozte do jednotlivych vetvi programu

    # Kamen tupi nuzky
    # Vyhra pocitace
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Rock crushes scissors, computer wins.")
        return "computer"
    # Vyhra hrace
    elif user_choice == "rock" and computer_choice == "scissors":
        print(f"Rock crushes scissors, {user_name} wins.")
        return user_name

    # Papir bali kamen
    # Vyhra pocitace
    elif user_choice == "rock" and computer_choice == "paper":
        print("Paper covers rock, computer wins!")
        return "computer"
    # Vyhra hrace
    elif user_choice == "paper" and computer_choice == "rock":
        print(f"Paper covers rock, {user_name} wins!")
        return user_name

    # Nuzky strihaji papir
    # Vyhra pocitace
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Scissors cuts paper, computer wins.")
        return "computer"
    # Vyhra hrace
    elif user_choice == "scissors" and computer_choice == "paper":
        print(f"Scissors cuts paper, {user_name} wins.")
        return user_name


if __name__ == "__main__":
    user_name = input("What's your name? ")
    user_choice = input(f"{user_name}, do you want to choose rock, paper or scissors? ")
    winner = play_rock_paper_scissor(user_name, user_choice)
