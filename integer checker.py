
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


target_score = int_check("enter an integer greater than or equal to 13 ")
print(target_score)
