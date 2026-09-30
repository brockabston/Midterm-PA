import random
# Constant menu dividers
DISPLAY_DIVIDER = "=" * 40
DISPLAY_SINGLE_DIVID = "-" * 40

# Display function


def display(doubloons, reputation):
    print(DISPLAY_DIVIDER)
    print("    Captain's Cove - Main Menu")
    print(DISPLAY_DIVIDER)
    print(f"    Doubloons: {doubloons}   Reputation: {reputation}")
    print(DISPLAY_SINGLE_DIVID)
    print("1. Dice Duel")
    print("2. Hire the Fleet")
    print("3. Leave the Cove")

# function for main menu


def main():
    doubloons = 12
    reputation = 0
    choice = ""
    while choice != "3":
        display(doubloons, reputation)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Welcome to Dice Duel!")
        elif choice == "2":
            print("Welcome to Hire the Fleet!")
        elif choice == "3":
            print("Cya! Good luck on your journey, Captain!")
        else:
            print("Invalid selection, Please select 1, 2, or 3")

# function for showing score and reputation


def show_score(doubloons, reputation):
    print(f"Doubloons: {doubloons}       Reputation: {reputation}")


def get_num(question, min, max):
    while True:
        choice = input(question).strip()

        if not choice.isdigit():
            print("Please enter a whole number! ")
        elif int(choice) < min or int(choice) > max:
            print(f"Please put any number from {min} to {max}!")
        else:
            return int(choice)

# yes no questions/making sure that the answer is a yes or no


def yes_or_no(question):
    while True:
        choice = input(question).strip().lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Please Enter either yes or no! ")


def game_over(doubloons, reputation):
    if reputation >= 30 or doubloons <= 0:
        return True
    else:
        return False

# inported randomizer, return dice roll but rolling a 6 earns 10


def die_roll():
    roll = random.randint(1, 6)
    if roll == 6:
        return 10
    else:
        return roll


def player_turn():
    player_score = die_roll() + die_roll()
    print(f"Your current score is {player_score_score}")
    while player_score < 21:
        if yes_or_no("Roll again? (Yes/no): "):
            player_score = player_score + die_roll()
            print(f"Your new total score is {player_score}! ")
        else:
            print(f"You decided to stand on {player_score}! ")
            break
    if player_score > 21:
        print("You busted! You will get luckier next time!")
    print(f"Final Score: {player_score}")
    return player_score


def opponent_turn():
    opponent_score = die_roll()+die_roll()
    print(
        f"Your opponent rolled a {opponent_score} with their first two rolls! ")
    while opponent_score < 17:
        print("Your opponent is rolling again!")
        opponent_score = opponent_score + die_roll()
        print(f"Oppenent's score is now {opponent_score}")
    if opponent_score == 21:
        print(f"Opponents Score: {opponent_score}, Uh Oh try and beat that! ")
    elif opponent_score > 21:
        print(f"Opponents Score: {opponent_score} , Your opponent busted!")
    else:
        print(f"Your opponents final roll total is {opponent_score}")
    return opponent_score


def die_winner(player_score, opponent_score):
    if player_score > 21:
        return False
    elif opponent_score > 21:
        return True
    elif player_score == 21 and opponent_score == 21:
        return True
    elif player_score > opponent_score:
        return True
    else:
        return False


# Main flow of Control
    # answer = yes_or_no("Test? (Yes/no): ")
    # print("You got:", answer)
    # for i in range(20):
    #     print(die_roll())
# result = opponent_turn()
# for i in range(3):
#     print(opponent_turn())
print(die_winner(22, 15))
print(die_winner(18, 23))
print(die_winner(21, 21))
print(die_winner(19, 17))
print(die_winner(18, 21))
print(die_winner(19, 19))
main()
