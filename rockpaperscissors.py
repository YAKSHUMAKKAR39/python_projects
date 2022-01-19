#Step 1 :Take input from user
#Step 2 :Randomly generate computer_pick using random.randint()
#Step 3 :Compare user_input with randomly generated computer_pick input
#Step 4 :Give point depending on the inputs and comparison
#Step 5 :Loop should run until user inputs q
#Step 6:Print the winner and score*/

import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while(True):
    user_input=input("Enter Rock/Paper/Scissors/Q").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked",computer_pick +".") #didnt use , in place of + as , will add an extra space bw value and "."
    if user_input=="rock":
        if computer_pick=="rock":
            continue
        elif computer_pick=="scissors":
            user_wins+=1
        elif computer_pick=="paper":
            computer_wins+=1
    if user_input=="paper":
        if computer_pick=="paper":
            continue
        elif computer_pick=="scissors":
            computer_wins+=1
        elif computer_pick=="rock":
            user_wins+=1
    if user_input=="scissors":
        if computer_pick=="scissors":
            continue
        elif computer_pick=="rock":
            computer_wins+=1
        elif computer_pick=="paper":
            user_wins+=1
print("\nYou won",user_wins,"times.")
print("Computer won",computer_wins,"times.")
if computer_wins>user_wins:
    print("\nYou lost!\n")
elif computer_wins<user_wins:
    print("\nYou won!\n")
else:
    print("\nIts a tie!\n")
print("Thanks for playing :)")
