import random


def roll():
    # grab a random number between 1 - 6
    result = random.randint(1, 6)
    return result


def two_rolls(who):
    # rolls 2 dice amd returns total + if we had a double roll

    double_score = "no"

    # rolls 2 dice
    roll_1 = roll()
    roll_2 = roll()

    # check for double score
    if roll_1 == roll_2:
        double_score = "yes"

    # find total points
    total_points = roll_1 + roll_2

    # show result
    print(f"{who}: {roll_1} & {roll_2} total: {total_points}")

    return total_points, double_score


def int_check(question):
    while True:

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


# main routine goes here
user_score = 0
com_score = 0

num_rounds = 0

target_score = int_check("enter a target score: ")
print(target_score)

while user_score < target_score and com_score < target_score:

    # add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"*** Round {num_rounds} ***")

    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")
