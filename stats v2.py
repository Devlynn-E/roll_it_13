def get_stats(stats_list):
    stats_list.sort()

    low = stats_list[0]
    high = stats_list[-1]
    average = sum(stats_list) / len(stats_list)

    return [low, high, average]


# create lists to hold user and com scores
user_scores = [1, 3, 4, 2, 5, 6]
com_scores = [10, 6, 7, 12, 6, 7]

# Loop six times - for testing purposes, ask the user to enter the
# score for the user and the com for each round
# for item in range(0, 6):
#     user_score = int(input("Enter the user score: "))
#     com_score = int(input(" Enter the computer's score: "))
#
#     # add user score to list of user scores
#     user_scores.append(user_score)
#
#     # same with com
#     com_scores.append(com_score)

# calculate the lowest, highest and average
# scores and display them.

user_stats = get_stats(user_scores)
com_stats = get_stats(com_scores)

print("📊📊📊 Game Statistics 📊📊📊 ")
print(f"\nUser - Lowest: {user_stats[0]}\t "
      f"Highest: {user_stats[1]}\t "
      f"Average: {user_stats[2]}")

print(f"\ncomputer - Lowest: {com_stats[0]}\t "
      f"Highest: {com_stats[1]}\t "
      f"Average: {com_stats[2]}")

print(f"\nUser's scores: {user_scores}")
print(f"computer's scores: {com_scores}")
