def diary():
    import pickle
    def add():
        f=open('username.dat','wb')
        us=input('enter username')
        pa=input('enter password')
        l1=[us,pa]
        pickle.dump(l1,f)
        f.close()
    add()
    
    import tkinter
    window=tkinter.Tk()
    window.title('DIARYLOCK')
    window.configure(bg='grey')
    L1=tkinter.Label(window,text='USERNAME').grid(column=0,row=0)
    txt1=tkinter.Entry(window,width=20)
    txt1.grid(column=1,row=0)
    L2=tkinter.Label(window,text='PASSWORD').grid(column=0,row=1)
    txt2=tkinter.Entry(window,width=20,show='*')
    txt2.grid(column=1,row=1)
    
    def diary_entry():
        f=open('username.dat','rb')
        l1=pickle.load(f)
        f.close()
        m=txt1.get()
        n=txt2.get()
        if m==l1[0] and n==l1[1]:  
            print("LET'S WRITE TODAY'S DIARY ENTRY")
            st=input(' ')
            l=st.split('.')
            try:
                f=open('diaryentry.dat','wb')
                pickle.dump(l,f)
                print('YOUR ENTRY IS SAFE')
            except :
                print('error occurd')
        else:
            print('INCORRECT USERNAME OR PASSWORD')
    def diary_read():
        f=open('username.dat','rb')
        l1=pickle.load(f)
        m=txt1.get()
        n=txt2.get()
        if m==l1[0] and n==l1[1]:
            f=open('diaryentry.dat','rb')
            l=pickle.load(f)
            st=''
            for i in l:
                st+=(i+'.')
            print(st)
        else:
            print('INCORRECT PASSWORD OR USERNAME')
        

        
    bt1=tkinter.Button(window,text='WRITE',fg='green',command=diary_entry).grid(columnspan=2)
    bt2=tkinter.Button(window,text='READ',fg='green',command=diary_read).grid(columnspan=2)
    window.mainloop()
diary()


