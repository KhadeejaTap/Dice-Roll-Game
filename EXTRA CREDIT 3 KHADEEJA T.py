
import random

dice_art = {
    1: ("-----------", 
        "|         |", 
        "|    o    |", 
        "|         |", 
        "-----------"
        ),
    2: ("-----------", 
        "|    o    |", 
        "|         |", 
        "|    o    |", 
        "-----------"
        ),
    3: ("-----------", 
        "|    o    |", 
        "|    o    |", 
        "|    o    |", 
        "-----------"
        ),
    4: ("-----------", 
        "| o     o |", 
        "|         |", 
        "| o     o |", 
        "-----------"
        ),
    5: ("-----------", 
        "| o     o |", 
        "|    o    |", 
        "| o     o |", 
        "-----------"
        ),
    6: ("-----------", 
        "| o     o |", 
        "| o     o |", 
        "| o     o |", 
        "-----------"
        ),
}


def roll_dice():
    total = 0
    rollsPic = []
    rollsNum = []
    for _ in range(3):
        roll = random.randint(1, 6)
        rollsPic.append(dice_art[roll])
        rollsNum.append(roll)
        total += roll
    return total, rollsPic, rollsNum

def game(finalU, finalA, draws):
    totalUser, rollsPicUser, rollsNumUser = roll_dice()
    print("Let's roll your dice!!! ")
    for lines in zip(*rollsPicUser):
        print("   ".join(lines))
    
    totalAi, rollsPicAi, rollsNumAi = roll_dice()
    print("It's AI's turn to roll the dice!!! ")
    for lines in zip(*rollsPicAi):
        print("   ".join(lines))

    print(f"You ({totalUser}) {', '.join(map(str, rollsNumUser))} - {', '.join(map(str, rollsNumAi))} ({totalAi}) AI")

    if totalUser > totalAi:
        print("You win!!!")
        finalU += 1
    elif totalAi > totalUser:
        print("AI wins...")
        finalA += 1
    else:
        print("A draw!?!")
        draws += 1

    return finalU, finalA, draws

def mainFunction():
    finalU = 0
    finalA = 0
    draws = 0
    run = 0

    while True:
        answer = input("Do you want to play? (Y/N) ").strip().upper()
        if answer == "Y":
            run += 1
            finalU, finalA, draws = game(finalU, finalA, draws)
            if finalA > 0:
                print(f"GRAND TOTAL AFTER THE RUN #{run}: YOU {finalU + draws} - {finalA + draws} AI (Win Ratio: {finalU / finalA:.2f})")
            else:
                print(f"GRAND TOTAL AFTER THE RUN #{run}: YOU {finalU + draws} - {finalA + draws} AI (Win Ratio: {finalU})")
        elif answer == "N":
            print("OK bye!")
            break
        else:
            print("Invalid input, please type 'Y' or 'N'.")

mainFunction()