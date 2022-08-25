

import tkinter
window=tkinter.Tk()
window.geometry('200x300')
window.title('STUDY TIME DETAILS')
window.configure(bg='grey')

import pickle
def subtimeday():
    subtime={}
    n=int(input('enter number of subjects'))
    for i in range (n):
        sub=input('ENTER SUBJECT: ')
        time=float(input('ENTER TIME IN HOURS'))
        subtime[sub]=time
    f=open('subtimeday.dat','wb')
    pickle.dump(subtime,f)
    f.close()

def subtimeweek():
    subtime={}
    n=int(input('enter number of subjects'))
    for i in range (n):
        sub=input('ENTER SUBJECT: ')
        time=float(input('ENTER TIME IN HOURS'))
        subtime[sub]=time
    f=open('subtimeweek.dat','wb')
    pickle.dump(subtime,f)
    f.close()

def subtimemonth():
    subtime={}
    n=int(input('enter number of subjects'))
    for i in range (n):
        sub=input('ENTER SUBJECT: ')
        time=float(input('ENTER TIME IN HOURS'))
        subtime[sub]=time
    f=open('subtimemonth.dat','wb')
    pickle.dump(subtime,f)
    f.close()

bt1=tkinter.Button(window,text='PER DAY',fg='brown',bg='yellow',command=subtimeday).grid(column=1,row=0)
bt2=tkinter.Button(window,text='PER WEEK',fg='brown',bg='yellow',command=subtimeweek).grid(column=2,row=0)
bt3=tkinter.Button(window,text='PER MONTH',fg='brown',bg='yellow',command=subtimemonth).grid(column=3,row=0)
window.mainloop()    
    
        
