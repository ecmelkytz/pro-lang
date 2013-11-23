def dene(x):
    say=0   
    for i in range(len(x)):
        ilk=x[0] 
        while ilk in x:
            bul=x.find(ilk)
            x=x[:bul]+x[bul+1:]
            say+=1    
        print (ilk,":",say)
        say=0
