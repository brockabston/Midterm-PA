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


def die_roll():
    roll = random.randint(1, 6)
    match roll:
        case 1:
            return roll = 1
        case 2:
            return roll = 2
        case 3:
            return roll = 3
        case 4:
            return roll = 4
        case 5:
            return roll = 5
        case 6:
            return roll = 10


# Main flow of Control
# answer = yes_or_no("Test? (Yes/no): ")
# print("You got:", answer)
main()
