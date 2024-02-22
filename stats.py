# create lists to hold user and com scores
user_scores = []
com_scores = []

# Loop six times - for testing purposes, ask the user to enter the
# score for the user and the com for each round
for item in range(0, 6):
    user_score = int(input("Enter the user score: "))
    com_score = int(input(" Enter the computer's score: "))

    # add user score to list of user scores
    user_scores.append(user_score)

    # same with com
    com_scores.append(com_score)

# calculate the lowest, highest and average
# scores and display them.

# start the lists
user_scores.sort()
com_scores.sort()

user_low = user_scores[0]
user_high = user_scores[-1]
user_average = sum(user_scores) / len(user_scores)

print(f"\nLow: {user_low}")
print(f"High: {user_high}")
print(f"Average: {user_average}")

print(f"\nUser's scores: {user_scores}")
print(f"computer's scores: {com_scores}")
