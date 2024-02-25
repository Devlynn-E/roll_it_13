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


def get_stats(stats_list):
    stats_list.sort()

    low = stats_list[0]
    high = stats_list[-1]
    average = sum(stats_list) / len(stats_list)

    return [low, high, average]


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


# main routine goes here
user_score = 0
com_score = 0

num_rounds = 0

# create lists to hold user and com scores
user_scores = []
com_scores = []
game_history = []

print("\n🎲🎲 Roll It 13 🎲🎲")
print()

wants_instructions = yes_no("Do you want to view the instructions? ")

if wants_instructions == "yes":

    instructions()

print()
target_score = int_check("enter a target score: ")
print()

# Loop game until we have a winner
while user_score < target_score and com_score < target_score:

    # add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"*** Round {num_rounds} ***")

    # start of a single round

    # starts 'pass' values
    user_pass = "no"
    com_pass = "no"

    input("Press <enter> to begin this round")

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

    # loop (while both user / ai have <= 13 points
    while com_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update
        # points / status
        if user_points == 13:
            user_pass = "yes"

        print()
        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type no to pass): ")

        else:
            roll_again = "no"

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

        else:
            # if user passes, we don't ask them again
            user_pass = "yes"

        if com_points >= 10 and com_points >= user_points:
            com_pass = "yes"

        elif com_pass == "yes":
            pass

        else:
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

        if com_pass == "yes" and user_pass == "yes":
            break

    # outside loop - double user points if they won and are eligible

    # show rounds result
    if user_points < com_points <= 13:
        print("sorry - you have lost this round and no points "
              "have been added to your total score."
              f" The computer's score has "
              f"increased by {com_points}"
              f" points.")

        add_points = com_points

    elif com_points < user_points <= 13:
        # checks if player is eligible for double points
        if double_points == "yes":
            user_points *= 2

        print(f"Yay! You won the round and {user_points} points have "
              f"been added to your score")

        add_points = user_points

    else:
        print(f"Hm... The round ended in a tie and {user_points}"
              f" have been awarded to everybody")

        add_points = user_points

    # record round result and add to history
    round_result = f"Round {num_rounds} - User: {user_points} \t Computer: {com_points}"
    game_history.append(round_result)

    # end of a single round

    # if com wins
    if user_points < com_points:
        com_score += add_points

    # if user wins
    elif user_points > com_points:

        user_score += add_points

    else:
        com_score += add_points
        user_score += add_points

    # add user score to list of user scores
    user_scores.append(user_score)

    # same with com
    com_scores.append(com_score)

print(f"\n🎲🎲🎲 FINAL SCORES : "
      f"User: {user_score} points | Computer: {com_score} points 🎲🎲🎲")
print()

show_history = yes_no("Do you want to see the game history? ")
if show_history == "yes":
    print("\nGame History")

    for item in game_history:
        print(item)

    print()


# calculate the lowest, highest and average
# scores and display them.

user_stats = get_stats(user_scores)
com_stats = get_stats(com_scores)

print("📊📊📊 Game Statistics 📊📊📊 ")
print(f"\nUser - Lowest score: {user_stats[0]}\t "
      f"Highest score: {user_stats[1]}\t "
      f"Average score: {user_stats[2]:.2f}")

print(f"\ncomputer - Lowest score: {com_stats[0]}\t "
      f"Highest score: {com_stats[1]}\t "
      f"Average score: {com_stats[2]:.2f}")
