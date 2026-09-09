import random
import time
import winsound

# Creates A Typing Effect To My Introduction
print("\033[96m", end="")
text ="LETS PLAY NUMBER GUESSING GAME !!"
for i in text:
    print(i, end="")
    winsound.Beep(800, 30)
    time.sleep(0.09)
print("")
time.sleep(1)
print("\033[91m", end="")
text ="Creater: KUNJAN POKHREL"
for i in text:
    print(i, end="")
    winsound.Beep(800, 30)
    time.sleep(0.09)
print("\033[0m")
print("")
time.sleep(1)
# Introduction Ends

while True:
    try:
        play = input("Would You Like To Play A Number Game?[y or n]: ").lower()
        if play in ["y", "n"]:
            break
        else:
            print("Please Enter y or n")
    except:
        print("Please Enter y or n")

while play == "y":
    while True:
        try:
            difficulty = int(input("Choose Difficulty: \n[1] Easy(0-50) \n[2] Medium(0-100) \n[3] Hard(0-500) \n[4]Impossible(0-100000) \nEnter Your Choice: "))
            if difficulty in range(1, 5):
                break
            else:
                print("Please Enter in the range (1-4)")
        except:
            print("Please Enter in the range (1-4)")
    if difficulty == 1:
        number = random.randint(0, 50)
        maximum = 50
    elif difficulty == 2:
        number = random.randint(0, 100)
        maximum = 100
    elif difficulty == 3:
        number = random.randint(0, 500)
        maximum = 500
    elif difficulty == 4:
        number = random.randint(0, 100000)
        maximum = 100000

    while True:
        try:
            guess = int(input("Guess The Number: "))
            if guess in range(0, maximum + 1):
                break
            else:
                print(f"Please Guess A Number From 0 to {maximum}")
        except:
            print("Please Guess a Valid Number")
    guesses = 1
    while guess != number:
        if guess < number:
            print("Try Higher")
            print()
        elif guess > number:
            print("Try Lower")
            print()
        guesses += 1
        while True:
            try:
                guess = int(input("Guess The Number: "))
                if guess in range(0, maximum + 1):
                    break
                else:
                    print(f"Please Guess A Number From 0 to {maximum}")
            except:
                print("Please Guess a Valid Number")
    print(f"Total guesses: {guesses}\nOMG DID U CHEAT..... ITS CORRECT\nThe Number Was {number}")
    winsound.Beep(1000, 300)
    winsound.Beep(1200, 300)
    winsound.Beep(1500, 500)
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break
print("\033[96mHope You Had Fun !!! \033[0m")