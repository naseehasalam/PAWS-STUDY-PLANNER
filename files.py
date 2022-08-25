import csv
import pickle
def details():
    f=open('data.csv','w',newline='')
    wr=csv.writer(f,delimiter=',')
    wr.writerow(['NAME','STREAM','SUB1','SUB2','SUB3','SUB4','SUB5'])
    f.close()
details()

def marksmonthly():
    f=open('markm.csv','w',newline='')
    wr=csv.writer(f,delimiter=',')
    wr.writerow(['SUBJECT','MARKS'])
    f.close()
marksmonthly()

def marksterminal():
    f=open('markt.csv','w',newline='')
    wr=csv.writer(f,delimiter=',')
    wr.writerow(['SUBJECT','MARKS'])
    f.close()
marksterminal()


def day():
    f=open('subtimeday.dat','wb')
    day={}
    pickle.dump(day,f)
    f.close()
day()

'''def week():
    f=open('subtimeweek.dat','wb')
    week={}
    pickle.dump(week,f)
    f.close()
week()'''
    
def month():
    f=open('subtimemonth.dat','wb')
    month={}
    pickle.dump(month,f)
    f.close()
month()
    




    
