def dene(x):
    top=0
    if x>0:
        for i in range(x):
            bol=x/2
            x=bol
            if bol>0.1:
                top+=bol
            else:
                pass
        return top    
    else:
        print ("pozitif tamsayı giriniz")

    
