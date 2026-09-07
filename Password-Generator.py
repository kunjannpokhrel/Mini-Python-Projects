import random
import time
import winsound
import string

# Creates A Typing Effect To My Introduction
print("\033[1m\033[96m", end="")
text = "PASSWORD GENERATOR!!"
for i in text:
    print(i, end="")
    winsound.Beep(800, 30)
    time.sleep(0.09)
print("")
time.sleep(1)
print("\033[91m", end="")
text = "Creator: KUNJAN POKHREL"
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
     length = int(input("Pick Your Password Length: "))
     break
    except ValueError:
     print("The number should be an integer.")
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
all_characters = lowercase + uppercase + numbers + special
print("Your password is","*"*length)
password = ""
for i in range(length):
 password += random.choice(all_characters)
name = input("Do You Want To Show Your Password? [y or n]: ").lower()
while name not in ["y", "n"]:
  print("Please enter y or n.")
  name = input("Do You Want To Show Your Password? [y or n]: ").lower()
if name == "y":
    print()
    print("Your Password:", password)
    print("\n\033[91mHOPE YOUR PASSWORD DOESN'T GET HACKED!!!\n\033[0m")
elif name == "n":
    hidden_password = ""
    for i in range(length):
     hidden_password += "*"

    print("Your Password:", hidden_password)