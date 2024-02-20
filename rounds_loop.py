
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

target_score = int_check("enter a target score: ")
print(target_score)

while user_score < target_score and com_score < target_score:
    print("Round heading goes here...")
    add_points = int(input("How many points have been won?"))
    user_score += add_points
