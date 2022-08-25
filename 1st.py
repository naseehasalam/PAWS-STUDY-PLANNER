import tkinter
window=tkinter.Tk()
window.title('Login Credentials')
L1=tkinter.Label(window,text='USERNAME').grid(column=0,row=0)
txt1=tkinter.Entry(window,width=20)
txt1.grid(column=1,row=0)
L2=tkinter.Label(window,text='PASSWORD').grid(column=0,row=1)
txt2=tkinter.Entry(window,width=20,show='*')
txt2.grid(column=1,row=1)
def clicked():
    m=txt1.get()
    n=txt2.get()
    if m=='naseeha' and n=='1234':
        import FINAL1
        FINAL1.studentdata()
    else:
        print('USERNAME AND PASSWORD INVALID')
        
bt=tkinter.Button(window,text='ENTER',fg='green',command=clicked).grid(columnspan=2)
    
    
