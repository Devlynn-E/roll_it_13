
while True:

    error = "please enter an integer 13 or above"
    try:
        # checks for an integer
        my_num = int(input("Enter an integer "))

        # checks that the number >= 13
        if my_num < 13:
            print(error)
            
        elif my_num >= 13:
            print("Your number is ", my_num)

    except ValueError:
        print(error)
        