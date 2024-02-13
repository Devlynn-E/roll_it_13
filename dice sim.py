import random


def roll():
    # grab a random number between 1 - 6
    result = random.randint(1, 6)
    return result


# main routine starts here
for item in range(0, 10):

    user_score = 0
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
    print(f"Die 1: {roll_1} \t Die 2: {roll_2} \t Points: {user_points}")
    print(f"Double score opportunity: {double_score}")
