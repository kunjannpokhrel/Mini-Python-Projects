import math
import time
import winsound

# Creates A Typing Effect To My Introduction
print("\033[96m", end="")
text ="MINI-CALCULATORRR !!"
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

def asmd():
    total = float(input("Enter starting number: "))
    while True:
        print(f"Current total: {total}")
        opr = input("Enter operation (+, -, *, /) or 'q' to quit: ").lower()
        if opr == 'q':
            break
        num = float(input("Enter next number: "))
        if opr == '+':
            total += num
        elif opr == '-':
            total -= num
        elif opr == '*':
            total *= num
        elif opr == '/':
            total /= num
    print(f"Final Total: {total}")

def main():
    print("--- Calculator ---") 
    option=int(input("1.Add/Subtract/Multiply/Divide\n2.Power\n3.log()\n4.Square-Root\n5.ln\n6.sin()\n7.cos()\n8.tan()\nChoose One: ") )
    if option==1:
     asmd()
    elif option==2:
        num = float(input("Enter your number: "))
        power= float(input("Power: "))
        ans=num**power
        print(f"Answer: {ans}")
    elif option==3:
        num = float(input("Enter your number: "))
        base = float(input("Enter your base: "))
        print(f"Answer: {math.log(num,base)}")
    elif option==4:
        num = float(input("Enter your number: "))
        print(f"Answer: {math.sqrt(num)}")
    elif option==5:
        num = float(input("Enter your number: "))
        print(f"Answer: {math.log(num)}")
    elif option==6:
        num = float(input("Enter your number: "))
        print(f"Answer: {math.sin(num)}")   
    elif option==7:
        num = float(input("Enter your number: "))
        print(f"Answer: {math.cos(num)}")      
    elif option==8:
        num = float(input("Enter your number: "))
        print(f"Answer: {math.tan(num)}")           
main()

print("\033[96mHope You Had Fun !!! \033[0m")
    
