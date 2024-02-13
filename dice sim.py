import random


def roll():
    # grab a random number between 1 - 6
    result = random.randint(1, 6)
    return result


def two_rolls():
    # rolls 2 dice amd returns total + if we had a double roll

    double_score = False

    # rolls 2 dice
    roll_1 = roll()
    roll_2 = roll()

    # check for double score
    if roll_1 == roll_2:
        double_score = True

    # find total points
    user_points = roll_1 + roll_2

    # show result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# main routine starts here
while True:

    how_many = int(input("1 or 2 dice? "))
    dice_error = "please pick 1 or 2 dice"

    if how_many == 2:
        start_points = two_rolls()
        points = start_points[0]
        double_points = start_points[1]

        print(f"You have {points} points and a double score of {double_points}")
        print()

    elif how_many == 1:
        start_points = roll()
        points = start_points

        print(f"You have {points} points")
        print()

    else:
        print(dice_error)
        print()

