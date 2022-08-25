from tkinter import *
import csv

    
window=Tk()
window.geometry('200x300')
window.configure(bg='grey')
window.title('MARKS')   
      
def addmarkm():
    f=open('markm.csv','w',newline='')
    wr=csv.writer(f,delimiter=',')
    wr.writerow(['SUBJECT','MARKS'])
    for i in range(5):
        sub=input('ENTER SUBJECCT: ')
        marks=input('ENTER MARKS: ')
        wr.writerow([sub,marks])
    print('DATA ADDED')
    

def addmarkt():
    f=open('markt.csv','w',newline='')
    wr=csv.writer(f,delimiter=',')
    wr.writerow(['SUBJECT','MARKS'])
    for i in range(5):
        sub=input('ENTER SUBJECCT: ')
        marks=input('ENTER MARKS: ')
        wr.writerow([sub,marks])
    print('DATA ADDED')
    

bt1=Button(window,text='MONTHLY MARK',fg='blue',command=addmarkm).grid(columnspan=2)
bt2=Button(window,text='TERMINAL MARK',fg='blue',command=addmarkt).grid(columnspan=2)
window.mainloop()


    
            
                    
        
        
