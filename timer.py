import time
import pickle
from datetime import date
print('WELCOME TO TIMER')
st=input("LET'S START? (y/n): ")
if st == 'y':
    start= True
t=int(input('ENTER FOR HOW MANY HOURS (only whole number)'))
sec=0
Min=0
start="True"
while start:
    sec+=1
    time.sleep(1)
    if sec==60:
        sec=0
        Min+=1
    if Min==60*t:
        print('YOU DID IT!')
        today=date.today()
        d4 = today.strftime("%b-%d-%Y")
        print(d4)
        break
        
