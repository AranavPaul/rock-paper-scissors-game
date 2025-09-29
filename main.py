##ROCK PAPER SCISSOR GAME

# Play with computer (Where computer will choose randomly, not conditionally)
#Get the input from users and print result

import random #Library


print("---Choose from Paper, Scissor, Rock---")

game_console = ''' 
     _______
    |.-----.|
    ||     ||
    ||_____/|
    | .     |
    |-|-  oo|
    |  _ _  |
    |       /
    `""""""`
''' #Tool used to exract this text - ASCII Art Archive
print (game_console)

user_choice = input("Enter your move: ")

computer_choice = random.choice (["Rock", "Paper", "Scissor"])

print(f"User's choice {user_choice} \nComputer's choice {computer_choice}")

if user_choice == "Rock" or user_choice == "rock":
    if computer_choice == "Rock":
        print ("It's a tie")
    elif computer_choice == "Paper":
        print ("Computer wins")
    else:
        print ("User wins")

elif user_choice == "Paper" or user_choice == "paper":
    if computer_choice == "Rock":
        print ("User wins")
    elif computer_choice == "Paper":
        print ("It's a tie")
    else:
        print ("Computer wins")

elif user_choice == "Scissor" or user_choice == "scissor":
    if computer_choice == "Rock":
        print ("Computer wins")
    elif computer_choice == "Paper":
        print ("User wins")
    else:
        print ("It's a tie")
else:
    print("Choose from 'Rock', 'Paper', 'Scissor'")



