import sys
import random
from enum import Enum

def rps():
        
    gamecount = 0
    playerwins = 0
    pythonwins = 0

    def play_rps():
        nonlocal playerwins
        nonlocal pythonwins

        class rps(Enum):
            rock = 1
            paper = 2
            scissors = 3

        player = int(input("enter 1 for rock, \n2 for paper, \n3 for scissors:\n"))

        if player not in [1,2,3]:
            print("you must enter 1/2/3.")
            return play_rps()

        computer = random.randint(1,3)


        print(f"\nYou chose {str(rps(player)).replace('rps.','').title()}.")
        print(f"\nPython chose {str(rps(computer)).replace('rps.','').title()}.\n")

        def winner(player, computer):
            nonlocal playerwins
            nonlocal pythonwins

            if player == computer:
                return "It is a draw!🫡"

            elif player == 1 and computer == 3:
                playerwins += 1
                return "You win!🎉"

            elif player == 2 and computer == 1:
                playerwins += 1
                return "You win!🎉"

            elif player == 3 and computer == 2:
                playerwins += 1
                return "You win!🎉"

            else:
                pythonwins += 1
                return("Python wins!😒")
            
        gameresult = winner(player, computer)

        print(gameresult)

        nonlocal gamecount
        gamecount += 1

        print(f"\nGame count: {str(gamecount)}")
        print(f"\nPlayer wins: {str(playerwins)}") 
        print(f"\nPython wins: {str(pythonwins)}")

        while True:
            again = input("\nDo you want to continue? (y/n)")
            if again.lower() not in ["y", "n"]:
                print("You must enter either y or n!")
                continue
            else:
                break

        if again.lower()== "y":
            return play_rps()
        else:
            print("Thank you for playing!\n")
            sys.exit("Bye! 🙋‍♀️")

    
    return play_rps()

r_p_s = rps()

if __name__ == "__main__":
    r_p_s()






