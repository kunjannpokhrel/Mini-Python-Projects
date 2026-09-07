import time
import winsound

# Creates A Typing Effect To My Introduction
print("\033[1m\033[96m", end="")
text ="TIMER FROM PYTHON!!"
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

min=-1
while min<0:
   min = int(input("Enter Minutes > 0: "))
   sec = int(input("Enter Seconds: "))
while min > 0 or sec > 0:
    print(f"{min:02d}:{sec:02d}........")
    time.sleep(1)
    if sec > 0:
        sec -= 1
    else:
        min -= 1
        sec = 59
print("00:00")
print("Time's up!")

# For Sound effect
winsound.Beep(1000, 500)
winsound.Beep(1000, 500)
winsound.Beep(1000, 1000)