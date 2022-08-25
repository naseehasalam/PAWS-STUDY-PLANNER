import pickle
import matplotlib.pyplot as plt

def subtimeday_plt():
    f=open('subtimeday.dat','rb')
    dict1=pickle.load(f)
    f.close()
    x=[]
    y=[]
    for i in dict1:
        x.append(i)
        y.append(dict1[i])
    plt.plot(x,y)
    plt.xlabel('subjects')
    plt.ylabel('number of hours')
    plt.title('sub-time')
    plt.show()


def subtimeweek_plt():
    f=open('subtimeweek.dat','rb')
    dict1=pickle.load(f)
    f.close()
    x=[]
    y=[]
    for i in dict1:
        x.append(i)
        y.append(dict1[i])
    plt.plot(x,y)
    plt.xlabel('subjects')
    plt.ylabel('number of hours')
    plt.title('sub-time')
    plt.savefig("week.png")
    plt.show()
def subtimemonth_plt():
    f=open('subtimemonth.dat','rb')
    dict1=pickle.load(f)
    f.close()
    x=[]
    y=[]
    for i in dict1:
        x.append(i)
        y.append(dict1[i])
    plt.plot(x,y)
    plt.xlabel('subjects')
    plt.ylabel('number of hours')
    plt.title('sub-time')
    plt.savefig("week.png")
    plt.show()
while True:
    print('ENTER ANY OTHER NUMBER THAN 1,2 TO EXIT')
    print('1.day_time graph')
    print('2.week_time graph')
    print('3.month_time graph')
    ch=int(input('ENTER YOUR CHOICE: '))
    if ch==1:
        subtimeday_plt()
    elif ch==2:
        subtimeweek_plt()
    elif ch==3:
        subtimemonth_plt()
    else:
        break
