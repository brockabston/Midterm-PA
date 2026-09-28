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


main()
