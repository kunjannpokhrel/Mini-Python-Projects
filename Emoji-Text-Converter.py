import demoji
import requests

url='https://www.emoji.family/api/emojis'
request= requests.get(url)
if request.status_code == 200:
 print("DATA RETRIVED FROM API")
 data= request.json()
else:
 print("EMOJI NOT FOUND")

def text():
    text= input("Enter The Emoji: ")
    emoji=demoji.findall(text)
    for i,j in emoji.items():
     print(f"{i} ---> {j}")

def emoji():
   text= input("Enter The Text: ")
   for i in data:
      for j in i.get('tags') or j in i.get('group') or j in i.get('subgroup') or j in i.get('annotation'): 
       if j == text:
        for t in i.get('emoji'):
         print(t, end=" ")

def main():
   choose=int(input("[1] Emoji --> Text \n[2]Text ---> Emoji \nCHOOSE ONE: "))
   if choose == 1 :
     text()
   if choose == 2 :
     emoji()

main()



