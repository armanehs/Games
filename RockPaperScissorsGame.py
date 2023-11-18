from random import random


if computerRandom > 0 and computerRandom <= 0.3:
    value1 = "Rock"
    if userChoice == "Rock".lower():
        print(f"you choose {userChoice} and computer choose was {value1}. Tie.")
    elif userChoice == "Paper".lower():
        print(f"you choose {userChoice} and computer choose was {value1}. you win.")
    elif userChoice == "Scissors".lower():
        print(f"you choose {userChoice} and computer choose was {value1}. you lose.")
elif computerRandom > 0.3 and computerRandom <= 0.6:
    value2 = "Paper"
    if userChoice == "Rock".lower():
        print(f"you choose {userChoice} and computer choose was {value2}. you lose.")
    elif userChoice == "Paper".lower():
        print(f"you choose {userChoice} and computer choose was {value2}. Tie.")
    elif userChoice == "Scissors".lower():
        print(f"you choose {userChoice} and computer choose was {value2}. you win.")
elif computerRandom > 0.6 and computerRandom < 1:
    value3 = "Scissors"
    if userChoice == "Rock".lower():
        print(f"you choose {userChoice} and computer choose was {value3}. you win.")
    elif userChoice == "Paper".lower():
        print(f"you choose {userChoice} and computer choose was {value3}. you lose.")
    elif userChoice == "Scissors".lower():
        print(f"you choose {userChoice} and computer choose was {value3}. Tie.")
        
