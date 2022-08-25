import pickle
from tkinter import *
from datetime import date
def todo_list():  
    window=Tk()
    window.title('TO DO LIST')
    window.geometry('200x300')
    window.configure(bg='grey')
    def to_do():
        n=int(input('ENTER NUMBER OF ACTIVITIES TO DO: '))
        dict1={}
        l1=[]
        for i in range(n):
            todo=input('ENTER ACTIVITY')
            l1.append(todo)
            today=date.today()
            d4 = today.strftime("%b-%d-%Y")
            dict1[d4]=todo
        f=open('todo.dat','wb')
        pickle.dump(dict1,f)
        f.close()
        def printc():
            print('HURRAY!!WORK DONE!')
        for i in range (len(l1)):
            but=Checkbutton(window,text=l1[i],command=printc).grid(column=0,row=i)
    bt1=Button(window,text='MAKE TO DO',command=to_do).grid(columnspan=2)
    window.mainloop()
todo_list()
            

            
            
        
    
