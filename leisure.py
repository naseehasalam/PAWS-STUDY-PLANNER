import random
def leisure():
    n=int(input('ENTER NUMBER OF LEISURE ACTIVITIES YOU WISH TO CHOOSE FROM'))
    l=[]
    for i in range (n):
        les=input('ENTER ACTIVITY NAME')
        l.append(les)
    print('LEISURE ACTIVITY CHOSEN IS')
    c=random.randint(0,len(l)-1)
    print(l[c])
leisure()
