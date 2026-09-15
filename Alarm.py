import datetime
import time
import winsound

target=input("Set Alarm [HH:MM:SS]: ")
print(f"The Alarm Is Set for {target}")

def alarm():
 for _ in range(20):
  print("The Time Is Up !!!!")
  winsound.Beep(2500, 150)
  time.sleep(0.05)  

running=True
while running==True:
    current=datetime.datetime.now().strftime("%H:%M:%S")
    print(current)
    time.sleep(1)
    if target==current:
     alarm()
     running= False


