import csv
def data():
    def studentdata():
        print('''WELCOME TO THE STUDY PLANNER , LETS START BY ENTERING THE FOLLOWING DATA''')
        print("0.NAME , 1.STREAM,2.HOBBIES, 3.HOURS FOR STUDY,4.WAKE UP TIME,5.SLEEP TIME",sep='/n')
    
        n=int(input('ENTER NUMBER OF STUDENTS: '))
        lmain=[]
        for i in range (n):
            name=input('ENTER NAME')
            stream=input('ENTER STREAM')
            hob=input('ENTER HOBBIE')
            hs=input('ENTER HOURS FOR STUDY')
            wt=input('ENTER WAKE UP TIME (in 12 hr format only one digit) ')
            st=input('ENTER SLEEP TIME (in 12 hr format only one digit)')
            l1=[name,stream,hob,hs,wt,st]
            lmain.append(l1)
        
        f=open('studentdata.csv','w',newline='')
        wr=csv.writer(f,delimiter=',')
        wr.writerow(['NAME','STREAM','HOBBIE','STUDYHOURS','WAKE UP','SLEEP'])
        wr.writerows(lmain)
        f.close()
    studentdata()

    def display():
        import tkinter
        window=tkinter.Tk()
        window.geometry('500x600')
        window.title('STUDENT DATA')

        f=open('studentdata.csv','r')
        rd=csv.reader(f,delimiter=',')
        l2=[]
        for row in rd:
            l2.append(row)
        for i in range (0,len(l2)):
            for j in range(len(l2[i])):
                l1=tkinter.Label(window,text=l2[i][j]).grid(column=j,row=i)     
        window.mainloop()        
    display()
data() 

    
               
                    
                
                
                 
        
    
    
        
        
    
