import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    a = 33
    b = 33 
    playerchoice = input("\n Ener....\n1 for Rock 2 for Paper 3 for Scissors")
    if playerchoice not in ["1" , "2", "3"]:
        print("you must enter 1 or 2 or 3")
        return play_rps()
    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\n You chose" + str(RPS(player)).replace('RPS.','').title()+".")
    print("\n Python Chose" + str(RPS(computer)).replace('RPS.','').title()+".")
    
if player == 1 and computer == 3:
	    print("You win")
elif player == 2 and computer == 3:
         print("you wind")
else:
         print("test")
    # elif player == 2 and computer == 1:
	#     print("you win")
    # elif player == computer:
	#     print("Tie")
    # else:
	#     print("python wins")
      
    

play_rps()
