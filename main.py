import pickle
import csv
import tkinter

import tkinter
print('WELCOME TO PAWS STUDY PLANNER')
print("THIS IS AN APP THAT HELP'S YOU TO ORGANIZE,ANALYZE AND IMPROVE YOUR STUDY PATTERN\nPAWS CAN BE YOUR STUDY COMPANION AND FRIEND")
print('IF NEW, START BY ADDING PERSONAL DETAILS TO ACCESS OTHER UTILITIES')
while True:
    print('1.ADD PERSONAL DETAILS')
    print('2.ADD STUDY DETAILS')
    print('3.ADD STUDY TIME DETAILS')
    print('4.ADD MARKS')
    print('5.MAKE TIMETABLE ')
    print('6.ANALYZE STUDY TIME')
    print('7.ANALYZE MARKS OBTAINED')
    print('8.LIESURE ACTIVITY SELECTOR')
    print('9.TIMER')
    print("10.DIARY")
    print('11.TO-DO LIST')
    print("12.ONLINE CLASS INFO")

    ch=int(input('ENTER YOUR CHOICE'))
    if ch==1:
        import FINAL1
    elif ch==2:
        import add
    elif ch==3:
        import timedata
    
    elif ch==4:
        import addmark
    elif ch==5:
        import timetable
        timetable.timetable()
    elif ch==6:
        import plotime
    elif ch==7:
        import plotmark
        plotmark.plot()
    elif ch==8:
        import leisure
    elif ch==9:
        import timer
    elif ch==10:
        import diary
        diary.diary()
    elif ch==11:
        import to_do
    elif ch==12:
        import information
        information.info()
    else:
        break
        

    


