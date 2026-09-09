import random
import time
import winsound

# Creates A Typing Effect To My Introduction
print("\033[96m", end="")
text ="LETS PLAY ROCK PAPER SCISSORS!!"
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
    while True:
     try :
         win_score=int(input("Set The Winning Score: "))
         if win_score>0:
             break
         else:
           print("")
           print("Please Pick A Positive number")
     except ValueError:
        print("")
        print("Please Pick A Positive number")
    player_score=0
    robot_score=0

    # Created Function compare()
    def compare():
      robot=random.randint(1,3)    
      while True:
        try :
          print("")
          player=int(input(" [1]ROCK ✌️ \n [2]PAPER ✋ \n [3]SCISSORS ✊\n Pick your move: "))
          if player in [1,2,3]:
              break
          else:
           print("Please pick 1, 2 or 3")
        except ValueError:
         print("")
         print("please pick 1 , 2 or 3 ")
      if  robot== player:
           print("ITS A LAME DRAWWW")
           return "draw"
      elif (robot == 1 and player == 2) or (robot == 3 and player == 1) or (robot == 2 and player == 3):
       print("\033[92mYOUU WONN !!!!\033[0m")
       return "win"
      elif (robot == 2 and player == 1) or (robot == 1 and player == 3) or (robot == 3 and player == 2):
       print("\033[91mYOU LOST !!!!\033[0m")
       return "lose"

    while robot_score!=win_score and player_score!=win_score:
      result = compare()
      if result == "win":
       player_score += 1
      elif result == "lose":
        robot_score += 1
      print(f"The SCORE Is {player_score} : {robot_score}")
      print("")
    print(f"FINAL SCORE {player_score} : {robot_score}")
    if player_score == win_score:
     winsound.Beep(1000, 300)
     winsound.Beep(1200, 300)
     winsound.Beep(1500, 500)
    else:
     winsound.Beep(500, 300)
     winsound.Beep(400, 500)
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        break
print("\033[96mHope You Had Fun !!! \033[0m")