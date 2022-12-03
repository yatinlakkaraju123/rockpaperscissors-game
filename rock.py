# this project simulates one player rock paper scissors game where your opponent is the computer
import random
print("enter\n1 for rock\n2 for scissors\n3 for paper\n4-1 to exit the game")
user_input = 0
while(user_input!=-1):
    try:
        user_input = int(input("its your turn:"))
        computer_output = random.randrange(1,3)
        if(user_input==1 and computer_output == 3):
            print("computer wins")
        elif(user_input == 2 and computer_output == 1):
            print("computer wins")
        elif(user_input == 3 and computer_output == 2):
            print("computer wins")
        elif(user_input==computer_output):
            print("its a tie")
        elif(user_input == -1):
            print("game exiting")
        else:
            print("you win")
    except:
        print("invalid input try again")

            
    


