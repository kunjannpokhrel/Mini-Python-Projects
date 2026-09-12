import requests
import time
import winsound

# Creates A Typing Effect To My Introduction
print("\033[96m", end="")
text ="WELCOME TO THE CURRENCY CONVERTER !!!!"
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
    currency_response= requests.get("https://api.frankfurter.dev/v2/currencies")
    currencies= currency_response.json()
    while True:
        old_currency= input("What currency are you converting FROM? [eg:USD,NPR]: ").upper()
        valid = False
        for currency in currencies:
            if currency["iso_code"] == old_currency:
                valid = True
                break
        if valid:
            break
        print("Currency not found")
    response= requests.get(f"https://api.frankfurter.dev/v2/rates?base={old_currency}")
    data= response.json()
    while True:
        new_currency= input("What currency are you converting TO? [eg:USD,NPR]: ").upper()
        for currency in data:
            if currency["quote"] == new_currency:
                rate = currency["rate"]
                break
        else:
            print("Currency not found")
            continue
        break
    while True:
        try:
            amount= float(input("How much money do you want to convert?: "))
            if amount> 0:
                break
            else:
                print("Please enter a positive amount.")
        except:
            print("Please enter a valid number.")
    new_amount=amount * rate
    print(f"{amount:.2f} {old_currency} = {new_amount:.2f} {new_currency}")
    winsound.Beep(700, 100)
    winsound.Beep(1000, 100)
    winsound.Beep(1400, 120)
    winsound.Beep(1800, 200)
    again = input("Would you like to try again?[y or n]: ").lower()
    if again != "y":
        break
print("\033[96mHope You Had Fun !!! \033[0m")