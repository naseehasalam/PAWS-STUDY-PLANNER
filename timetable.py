def timetable():
    import csv
    dict1={}
    l1=[]
    f=open('data.csv','r')
    rd=csv.reader(f,delimiter=',')
    next(rd)
    for row in rd:
        l1=row[2:7]
    print(l1)
    print('ENTER NUMBER HOURS CORRESPONDING TO EACH SUBJECT ')
    
    l2=[]
    for i in range (len(l1)):
        t=int(input('enter number of hours'))
        l2.append(t)
        dict1[l1[i]]=t
    f.close()
    print(l2)
    print(dict1)
    l=l2
    
    f=open('studentdata.csv','r')
    rd=csv.reader(f,delimiter=',')
    for row in rd:
        w=row[4]
        s=row[5]
    for i in range(len(l)):
        if i==0:
            t1=int(w)+l[i]
            t2=t1+l[i+1]
            t3=int(s)-(l[i+2]+l[i+3]+l[i+4])-1
            t4=int(s)-(l[i+3]+l[i+4])-1
            t5=int(s)-(l[i+4])-1
        else:
            break
        
    l3=[t1,t2,t3,t4,t5]
    print(l3)

    
    def display():
        import tkinter 
        window=tkinter.Tk()
        window.geometry('200x300')
        window.configure(bg='grey')
        window.title('TIMETABLE')

        L1=tkinter.Label(window,text=l1[0]).grid(column=0,row=0)
        L2=tkinter.Label(window,text=(w,'am','-', l3[0],'am')).grid(column=1,row=0)
        L3=tkinter.Label(window,text=l1[1]).grid(column=0,row=1)
        L4=tkinter.Label(window,text=(l3[0],'am','-', l3[1],'am')).grid(column=1,row=1)
        L5=tkinter.Label(window,text=l1[2]).grid(column=0,row=2)
        L6=tkinter.Label(window,text=(l3[2],'pm','-', l3[3],'pm')).grid(column=1,row=2)
        L7=tkinter.Label(window,text=l1[3]).grid(column=0,row=3)
        L8=tkinter.Label(window,text=(l3[3],'pm','-', l3[4],'pm')).grid(column=1,row=3)
        L9=tkinter.Label(window,text=l1[4]).grid(column=0,row=4)
        L10=tkinter.Label(window,text=(l3[4],'pm','-', s,'pm')).grid(column=1,row=4)
        window.mainloop()
    display()
           
timetable()      
    
    
    
    
