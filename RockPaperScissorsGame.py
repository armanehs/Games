# This is updateded version of Rock Paper Scissors game with GUI.

from random import randint
from tkinter import *

# Here we start to make the overall appearance of the program and describe what it should look like.
root=Tk()
root.title("Rock Paper Scissors")
root.geometry("250x250")
root.resizable(0,0)
root.config(bg="blue", bd=10, relief="groove")

# We make 3 functions and each function works only for one button.
def first():
    computerChoice = randint(1, 3)
    userChoice = "Rock"
    
    if computerChoice == 1:
        print(f"you coohse {userChoice} and computer choose Rock. Tie.")
    elif computerChoice == 2:
        print(f"you choose {userChoice} and computer choose Paper. you lose.")
    elif computerChoice == 3:
        print(f"you choose {userChoice} and computer choose Scissors. you win.")
        
def second():
    computerChoice = randint(1, 3)
    userChoice = "Paper"
    
    if computerChoice == 1:
        print(f"you coohse {userChoice} and computer choose Rock. you win.")
    elif computerChoice == 2:
        print(f"you choose {userChoice} and computer choose Paper. Tie.")
    elif computerChoice == 3:
        print(f"you choose {userChoice} and computer choose Paper. you lose.")        

def third():
    computerChoice = randint(1, 3)
    userChoice = "scissors"
    
    if computerChoice == 1:
        print(f"you coohse {userChoice} and computer choose Rock. you lose.")
    elif computerChoice == 2:
        print(f"you choose {userChoice} and computer choose Paper. you win.")
    elif computerChoice == 3:
        print(f"you choose {userChoice} and computer choose Scissors. Tie.") 
        
# We will create 3 buttons here. And we describe what each one should do.
rock = Button(root, text="Rock", command=first)
rock.pack()
paper = Button(root, text="Paper", command=second)
paper.pack()
Scissors = Button(root, text="Scissors", command=third)
Scissors.pack()
turn_off = Button(root, text="Quit", command=root.quit)
turn_off.pack()

root.mainloop()
# END