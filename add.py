
import csv
import pickle as p
import tkinter
window=tkinter.Tk()
window.geometry('500x400')
window.configure(bg='grey')
window.title('ADD DETAILS')
def ad_details():
    f=open('data.csv','w',newline='')
    wr=csv.writer(f,delimiter=',')
    wr.writerow(['NAME','STREAM','SUB1','SUB2','SUB3','SUB4','SUB5'])
    name=input('ENTER NAME: ')
    stream=input('ENTER STREAM: ')
    sub1=input('ENTER SUB1: ')
    sub2=input('ENTER SUB2: ')
    sub3=input('ENTER SUB3: ')
    sub4=input('ENTER SUB4: ')
    sub5=input('ENTER SUB5: ')
    l=[name,stream,sub1,sub2,sub3,sub4,sub5]
    wr.writerow(l)
    f.close()
    def display():
        window=tkinter.Tk()
        window.geometry('500x600')
        window.title('STUDENT DATA')

        f=open('data.csv','r')
        rd=csv.reader(f,delimiter=',')
        l2=[]
        for row in rd:
            l2.append(row)
        for i in range (0,len(l2)):
            for j in range(len(l2[i])):
                l1=tkinter.Label(window,text=l2[i][j]).grid(column=j,row=i)     
        window.mainloop()
        f.close()
    print('DATA DISPLAYED')
    display()

    
bt1=tkinter.Button(window,text='ADD STUDYDATA',fg='blue',command=ad_details).grid(columnspan=2)
window.mainloop()

