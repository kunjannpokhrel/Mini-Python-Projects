import time
import random
import winsound

# Starts Introduction
print("\033[1m\033[96m", end="")
text ="WELCOME TO MY GAME(QUIZ)!!"
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
# End Introduction

play=(input("Would You Like To Take A Math Quiz?[y or n]: "))
while play not in ["y", "n"]:
    print("Please enter only y or n.")
    play = input("Would You Like To Take A Math Quiz? [y or n]: ")
while play=="y":
    while True:
     difficulty= input("[1] Easy \n[2] Medium \n[3] Hard \nChoose Your Difficulty Level: ")
     if difficulty in ["1", "2", "3"]:
        break
     print("Please choose 1, 2, or 3.")
    while True:
     try:
        limit = int(input("Pick Time Limit In Seconds: "))
        if limit > 0:
            break
        print("Time must be greater than 0.")
     except ValueError:
        print("Please enter a number.")
    operators=["*","+","-"]
    count=0
    total=0
    start= time.time()
    while time.time()-start < limit:
     if difficulty in ["1"]:
           x = random.randint(0, 10)
           y = random.randint(0, 10)
     elif difficulty in ["2"]:
           x = random.randint(0, 50)
           y = random.randint(0, 50)
     elif difficulty in ["3"]:
           x = random.randint(0, 99)
           y = random.randint(0, 10)
           z = random.randint(0, 5)
     operator=random.choice(operators)
     if  difficulty in ["1","2"]:
         try: 
             ans = int(input(f"{x}{operator}{y}= "))
         except ValueError:
             ans = None   
         if operator == "+":
                 correct = x + y
         elif operator == "-":
                 correct = x - y
         elif operator == "*":
                 correct = x * y

     if  difficulty in ["3"]:
         try: 
             ans = int(input(f"{x}{operator}{y}{operator}{z}= "))
         except ValueError:
             ans = None   
         if operator == "+":
           correct = x + y + z
         elif operator == "-":
          correct = x - y - z
         elif operator == "*":
          correct = x * y * z

     if ans == correct:
         count += 1
     total+=1
    winsound.Beep(1000, 100)
    winsound.Beep(1000, 100)
    winsound.Beep(1000, 200)
    print("\n Time\'s up .....")
    print(" Total attempts: ",total ,"\n Correct: ",count ,"\n Time limit: ",limit,"seconds")
    time.sleep(2)
    while True:
     play = input("\nWould You Like To Play Again [y or n]: ")
     if play in ["y", "n"]:
        break
     print("Please enter only y or n.")
print("\n\033[91mOk!!! That's ENOUGH MATHS For A While\n\033[0m")