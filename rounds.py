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
    user_points = roll_1 + roll_2

    # show result
    print(f"{who}: {roll_1} & {roll_2}")

    return user_points, double_score


# main routine starts here
print("\n🎲🎲 Roll It 13 🎲🎲")
print()

print("Press <enter> to begin this round")
input()

# get start dice rolls
user_first = two_rolls("User")
user_points = user_first[0]
double_points = user_first[1]

# tell the user if they're eligible for double points
if double_points == "yes":
    print("If you win this round, you gain double points!")

# output first move results

# get start dice rolls for ai
com_first = two_rolls("Computer")
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

        # if points over 13, resets points and tells the player
        if user_points > 13:
            print(f"*** oops! You rolled a {user_move} so your total is {user_points}. "
                  f"Which is over 13 points. ***")

            user_points = 0

            break

        elif user_points == 13:
            print(f"!!! Yay! You rolled a {user_move}, so you now have 13 points. "
                  f"You win! !!!")

            break

        print(f"You rolled a {user_move}. You now have {user_points} points.")

    print("\nPress <enter> to continue...")
    input()

    # roll die for AI and update AI points
    com_move = roll()
    com_points += com_move

    if com_points > 13:
        print(f"!!! Yay! The computer rolled a {com_move} and now has {com_points} points. "
              f"which is over 13 points. !!!")

        com_points = 0

        break

    print(f"The computer rolled a {com_move}. The computer"
          f" now has {com_points}.")

    print()
    if com_points < user_points:
        result = "You are ahead."

    elif com_points > user_points:
        result = "The computer is ahead"

    else:
        result = "It's currently a tie."

    print(f"*** Round Update ***: {result}")
    print(f"User Score: {user_points} \t | \t Computer Score: {com_points}")

# outside loop - double user points if they won and are eligible

# show rounds result
if user_points < com_points <= 13:
    print("sorry - you have lost this round and no points "
          "have been added to your total score. The computer's score has "
          f"increased by {com_points}"
          f" points.")

elif com_points < user_points <= 13:
    # checks if player is eligible for double points
    if double_points == "yes":
        user_points *= 2
        
    print(f"Yay! You won the round and {user_points} points have "
          f"been added to your score")

else:
    print(f"Hm... The round ended in a tie and no points have been awarded")

