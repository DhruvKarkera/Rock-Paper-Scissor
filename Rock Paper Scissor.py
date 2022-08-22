from random import randint
import time

list = ["Rock", "Paper", "Scissor"]

computer =list[randint(0,2)]

player = False

while player == False :
    player = input("Rock,Paper,Scissor?")
    if player== computer :
        print("TIE!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer Chooses", computer)
            time.sleep(2)
            print("You lose", computer, "Covers", player)
        else:
             print("Computer chooses", computer)
             time.sleep(2)
             print("You Win! ", player,"smashes",computer)
    elif player == "Scissor":
        if computer == "Rock":
            print("Computer chooses", computer)
            time.sleep(2)
            print(" You lose", computer,"smashed", player)
        else:
            print("Computer chooses", computer)
            time.sleep(2)
            print("You win ", player,"cut", computer)
    else:
        if computer == "Scissor":
            print("Computer chooses")
            time.sleep(2)
            print("You lose", computer,"cut", player)
        else:
            print("Computer chooses", computer)
            time.sleep(2)
            print("You lose", computer,"cut", player)
    
           
            
            
            
