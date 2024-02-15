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


def roll():
    # grab a random number between 1 - 6
    result = random.randint(1, 6)
    return result


def two_rolls():
    # rolls 2 dice amd returns total + if we had a double roll

    double_score = "no"

    # rolls 2 dice
    roll_1 = roll()
    roll_2 = roll()

    # check for double score
    if roll_1 == roll_2:
        double_score = "yes"

    # find total points
    user_points = roll_1 + roll_2

    # show result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# main routine starts here
print("\n🎲🎲 Roll It 13 🎲🎲")
print()

print("Press <enter> to begin this round")
input()

# get start dice rolls
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# tell the user if they're eligible for double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points!"

# output first move results
print(f"You rolled a total of {user_points}. {double_feedback}")

# get start dice rolls for ai
com_first = two_rolls()
com_points = com_first[0]

print(f'the computer rolled a total of {com_points}.')

# loop (while both user / ai have <= 13 points
while com_points < 13 and user_points < 13:

    # ask user if they want to roll again, update
    # points / status
    print()
    roll_again = input("Do you want to roll the dice (type no to pass): ")
    if roll_again == "yes":
        user_move = roll()
        user_points += user_move
        print(f"You rolled a {user_move}. You now have {user_points} points.")

    print("\nPress <enter> to continue...")
    input()

    # roll die for ai and update ai points
    com_move = roll()
    com_points += com_move
    print(f"The computer rolled a {com_move}. The computer"
          f" now has {com_points}.")

    print()
    if user_points > com_points:
        result = "You are ahead."
    else:
        result = "The computer is ahead"

    print(f"*** Round Update ***: {result}")
    print(f"User Score: {user_points} \t | \t Computer Score: {com_points}")

# outside loop - double user points if they won and are eligible

# show rounds result
if user_points < com_points:
    print("sorry - you have lost this round and no points "
          "have been added to your total score. The computer's score has "
          f"increased by {com_points} points.")

# currently does not include double points
else:
    print(f"Yay! You won the round and {user_points} points have "
          f"been added to your score")
