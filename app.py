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


def dice_duel(doubloons, reputation):
    print(DISPLAY_DIVIDER)
    print(f"     Welcome to dice duel Captain!")
    print(DISPLAY_DIVIDER)
    show_score(doubloons, reputation)
    print(DISPLAY_SINGLE_DIVID)
    print("      Rules for Dice Duel")
    print(DISPLAY_SINGLE_DIVID)
    print("Rule 1: You may only bet doubloons you have currently!")
    print("Rule 2: You start by rolling two die and try to get as close to 21 as possible!")
    print("Rule 3: You can chose to roll again once as many times as you want with each adding to your previous rolls that turn! But be careful, going over 21 means you bust and lose!")
    print("Rule 4: Ties result in a rival captain win. The only exception is if you both finish with a 21, you beat the rival captain! ")
    print("Rule 5: Die rolls are equal to the number you roll, except rolling a 6 is counted as 10 towards your total.")
    print("Rule 6: The rival captain always rolls after you have already gotten your total. ")
    print("Rule 7: The rival captain keeps rolling until their score is 17 or more. ")
    print("Rule 8: If you bust, the game ends. The rival captain will not roll as you lose as soon as you bust. ")
    print("Rule 9: If the rival busts, you win! ")


# Main flow of Control
    # answer = yes_or_no("Test? (Yes/no): ")
    # print("You got:", answer)
    # for i in range(20):
    #     print(die_roll())
# result = opponent_turn()
# for i in range(3):
#     print(opponent_turn())
dice_duel(12, 0)
main()
