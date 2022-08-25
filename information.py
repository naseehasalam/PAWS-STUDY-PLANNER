def info():
    import pickle
    import tkinter
    window=tkinter.Tk()
    window.geometry('200x300')
    window.configure(bg='grey')
    window.title('ONLINE CLASS INFO')
    def google_meet():
        dict1={}
        for i in range (5):
            sub=input('ENTER SUBJECT')
            code=input('ENTER CODE')
            dict1[sub]=code
            
        f=open('googlemeet.dat','wb')
        pickle.dump(dict1,f)
        f.close()
    

    def class_room():
        dict1={}
        for i in range (5):
            sub=input('ENTER SUBJECT')
            code=input('ENTER CODE')
            if code.isalnum():
                dict1[sub]=code
            else:
                print('INVALID CODE')
        f=open('classroom.dat','wb')
        pickle.dump(dict1,f)
        f.close()
        
   
    def display():
        print('1.GOOGLE MEET')
        f=open('googlemeet.dat','rb')
        d=pickle.load(f)
        for i in d:
            print('SUB',i,'\t\t','CODE: ',d[i])
        f.close()

            
        
        print('3.CLASSROOM')         
        f3=open('classroom.dat','rb')
        d3=pickle.load(f3)
        for i in d3:
            print('SUB',i,'\t\t',d3[i])
        f3.close()

       
    
    bt1=tkinter.Button(window,text='GOOGLE MEET',command=google_meet).grid(columnspan=2)
    bt3=tkinter.Button(window,text='CLASSROOM',command=class_room).grid(columnspan=2)
    bt6=tkinter.Button(window,text='DISPLAY',command=display).grid(columnspan=2)
info()       

            
        
            
            
    
    
