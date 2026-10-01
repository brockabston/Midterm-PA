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


def main():  # navigating main menu and making sure no incorrect inputs
    doubloons = 12
    reputation = 0
    choice = ""
    while choice != "3":
        display(doubloons, reputation)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # returns totals and updates them
            doubloons = dice_duel(doubloons, reputation)
        elif choice == "2":
            print("Welcome to Hire the Fleet!")
        elif choice == "3":  # ends app
            print("Cya! Good luck on your journey, Captain!")
        else:
            print("Invalid selection, Please select 1, 2, or 3")
        if reputation > 30:  # 30 or more reputation means you win and closes app
            print("Congrats, You Won! Youre the best and coolest captain on the sea!!!")
            break
        elif doubloons <= 0:  # ends app if doubloons are 0 or less
            print("Game over! You ran out of doubloons. Please restart and try again!")
            break


def show_score(doubloons, reputation):  # prints current score and reputation
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


def yes_or_no(question):    # yes no questions/making sure that the answer is a yes or no
    while True:
        choice = input(question).strip().lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Please Enter either yes or no! ")


# if doubloons fall to zero or below, ends game. If reputaion hits 30 or above, ends game
def game_over(doubloons, reputation):
    if reputation >= 30 or doubloons <= 0:
        return True
    else:
        return False


def die_roll():  # random number generator for dice rolls, inported randomizer, return dice roll nun but rolling a 6 earns 10
    roll = random.randint(1, 6)
    if roll == 6:
        return 10
    else:
        return roll


def player_turn():  # players turn, busts if players score is over 21, asks to roll again
    player_score = die_roll() + die_roll()
    print(f"Your current score is {player_score}")
    while player_score < 21:
        if yes_or_no("Roll again? (Yes/no): "):
            player_score = player_score + die_roll()
            print(f"Your new total score is {player_score}! ")
            print(DISPLAY_SINGLE_DIVID)
        else:
            print(f"You decided to stand on {player_score}! ")
            print(DISPLAY_SINGLE_DIVID)
            break
    if player_score > 21:
        print("You busted! You will get luckier next time!")
    print(f"Your final Score: {player_score}")
    print(DISPLAY_SINGLE_DIVID)
    return player_score


def opponent_turn():  # opponents turn, rolls till 17 or over
    opponent_score = die_roll()+die_roll()
    print(
        f"Your opponent rolled a {opponent_score} with their first two rolls! ")
    while opponent_score < 17:
        print("Your opponent is rolling again!")
        opponent_score = opponent_score + die_roll()
        print(f"Oppenent's score is now {opponent_score}")
        print(DISPLAY_SINGLE_DIVID)
    if opponent_score == 21:
        print(f"Opponents Score: {opponent_score}, Uh Oh try and beat that! ")
    elif opponent_score > 21:
        print(f"Opponents Score: {opponent_score} , Your opponent busted!")
    else:
        print(f"Your opponents final roll total is {opponent_score}")
        print(DISPLAY_DIVIDER)
    return opponent_score


def die_winner(player_score, opponent_score):  # decides winner of dice duel
    if player_score > 21:  # player busts
        return False
    elif opponent_score > 21:  # opponent busts
        return True
    elif player_score == 21 and opponent_score == 21:  # you and opponent tie, so you win
        return True
    elif player_score > opponent_score:  # you beat opponent
        return True
    else:  # anything else is situations you lose in
        return False


def dice_duel(doubloons, reputation):  # main dice duel game function
    print(DISPLAY_DIVIDER)
    print(f"     Welcome to dice duel Captain!")
    print(DISPLAY_DIVIDER)
    show_score(doubloons, reputation)
    print(DISPLAY_SINGLE_DIVID)
    print("       Rules for Dice Duel")  # lists rules
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
    print(DISPLAY_SINGLE_DIVID)
    print("Now that you've seen the rules, place your wager when you're ready to start!")
    round_doubloons = doubloons
    while True:
        # bet amount is pulling get num to make sure bet is in between min and max
        bet_amount = get_num("Place your wager: ", 1, doubloons)
        player_score = player_turn()  # gets player score
        if player_score > 21:  # checks if bust
            opponents_score = "DNR"  # DNR = Did not roll because player busted
        else:
            opponents_score = opponent_turn()
        # if die winner is true then that means the player won and gains wager. if false, opponent wins and wager is subtracted
        if die_winner(player_score, opponents_score):
            doubloons = doubloons + bet_amount
            print(f"You win! You gained {bet_amount} doubloons!")
        else:
            doubloons = doubloons - bet_amount
            print(f"Your rival beat you. You lose {bet_amount} doubloons. ")
        show_score(doubloons, reputation)
        if game_over(doubloons, reputation):  # checks to see if game ending conditions are true
            break
        # if no is said then it backs out
        if not yes_or_no("Want to play Dice Duel again? (yes/no): "):
            break
    print(DISPLAY_SINGLE_DIVID)
    this_round = doubloons - round_doubloons
    if this_round >= 0:
        print(f"This round you gained {this_round} doubloons")
    else:
        print(f"Arghhh This round you lost {this_round} doubloons")
    print(DISPLAY_SINGLE_DIVID)
    show_score(doubloons, reputation)
    return doubloons


# Main flow of Control
main()
