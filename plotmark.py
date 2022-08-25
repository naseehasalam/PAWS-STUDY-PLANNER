def plot():
    import matplotlib.pyplot as plt
    import csv
    def plotm():
        f=open('markm.csv','r')
        rd=csv.reader(f,delimiter=',')
        x=[]
        y=[]
        for row in rd:
            x.append(row[0])
            y.append(row[1])
        plt.bar(x,y,color='blue')
        plt.xlabel('SUBJECT')
        plt.ylabel('MARKS')
        plt.show()

    def plott():
        f=open('markt.csv','r')
        rd=csv.reader(f,delimiter=',')
        x=[]
        y=[]
        for row in rd:
            x.append(row[0])
            y.append(row[1])
        plt.bar(x,y,color='blue')
        plt.xlabel('SUBJECT')
        plt.ylabel('MARKS')
        plt.show()
    

    while True:
        print('TO EXIT ENTER ANY OTHER NUMBER THAN 1,2')
        print('1.MONTHLY MARK')
        print('2.TERMINAL MARK')
        ch=int(input('enter choice'))
        if ch==1:
            plotm()
        elif ch==2:
            plott()
        else:
            break
                
