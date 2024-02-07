
print("🎲🎲 Roll It 13 🎲🎲")
# defines what is a valid response
yes = ["y", "yes"]
no = ["n", "no"]

instructions = input("would you like to see instructions? ").lower()

if instructions in no:
    print()
elif instructions in yes:
    print()
    print('''
    
    **** instructions ****
    
    At the start of each round, the user and the computer each roll two dice.  
    The initial number of points for each player is the total shown by the dice.  Then, taking turns, 
    the user and computer each roll a single die and add the result to their points.  
    The goal is to get 13 points (or slightly less) for a given round.  
    Once you are happy with your number of points, you can ‘pass’.
    
    - If you go over 13, then you lose the round (and get zero points).
     
    - If the computer goes over 13, the round ends and your score is the number of points that you have earned.
    
    - If the computer gets more points than you eg: you get 10 and they get 11, then you lose your score stays the same 
    
    - If you get more points than the computer (but less than 14 points), you win and add your points to your score.  
      The computer’s score stays the same. 
      
    - If the first roll of your dice is a double, then your score is increased by double the number of points,
      provided you win.  If the computer’s first roll of the dice is a double, then its points are not doubled 
      (this gives the human player a slight advantage).
    
    - The ultimate winner of the game is the first one to get to the specified score goal.

    ''')
else:
    print("please answer yes or no to the question")

# main code
