import random


def int_check(question):
    while True:
        # checks for an integer above a certain number
        error = "please enter an integer 13 or above"

        try:
            # checks for an integer
            response = int(input(question))

            # checks that the number >= 13
            if response >= 13:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def yes_no(question):
    # starts loop
    while True:
        response = input(question).lower()

        # defines
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes or no")


def instructions():

    print('''

        **** instructions ****

        At the start of each round, the user and the computer each roll two dice.  
        The initial number of points for each player is the total shown by the dice.  Then, taking turns, 
        the user and computer each roll a single die and add the result to their points.  
        The goal is to get 13 points (or slightly less) for a given round.  
        Once you are happy with your number of points, you can ‘pass’.

        - If you go over 13, then you lose the round (and get zero points).

        - If the computer goes over 13, the round ends and your score is the number of points that you have earned.

        - If the computer gets more points than you eg: you get 10 and they get 11, 
          then you lose your score stays the same 

        - If you get more points than the computer (but less than 14 points), you win and add your points to your score.  
          The computer’s score stays the same. 

        - If the first roll of your dice is a double, then your score is increased by double the number of points,
          provided you win.  If the computer’s first roll of the dice is a double, then its points are not doubled 
          (this gives the human player a slight advantage).

        - The ultimate winner of the game is the first one to get to the specified score goal.

        ''')


def roll():
    # grab a random number between 1 - 6
    result = random.randint(1, 6)
    return result


def two_rolls():
    # rolls 2 dice amd returns total + if we had a double roll

    double_score = " not"

    # rolls 2 dice
    roll_1 = roll()
    roll_2 = roll()

    # check for double score
    if roll_1 == roll_2:
        double_score = ""

    # find total points
    user_points = roll_1 + roll_2

    # show result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# main routine starts here
print("\n🎲🎲 Roll It 13 🎲🎲")
print()

wants_instructions = yes_no("Do you want to view the instructions? ")

if wants_instructions == "yes":

    # displays instructions

    instructions()

# get start dice rolls
# tell the user if they're eligible for double points

dice_error = "please pick 1 or 2 dice"

how_many = int(input("1 or 2 dice? "))

if how_many == 2:
    start_points = two_rolls()
    points = start_points[0]
    double_points = start_points[1]

    print(f"You have {points} points and your{double_points} eligible for double points")
    print()

elif how_many == 1:
    start_points = roll()
    points = start_points

    print(f"You have {points} points")
    print()

else:
    print(dice_error)
    print()

# get start dice rolls for ai

# loop (while both user / ai have <= 13 points
    # ask user if they want to roll again, update
    # points / status

    # roll die for ai and update ai points

# outside loop - double user points if they won and are eligible
