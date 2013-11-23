def mutlak_genel():
    while True:
        sayi=input("karmaþýk sayýlar için 1,tamsayýlar için 2"\
                   "ondalýk sayýlar için 3,çýkmak için 4 giriniz:")
        if sayi==1:
            a=int(raw_input("Gerçel kýsmý giriniz:"))
            b=int(raw_input("Sanal kýsmý giriniz:"))
            z=float((a**2+b**2)**0.5)
            print "Karmaþýk sayýnýn mutlak deðeri:",z
        
        elif sayi==2:
            tamsayi=int(raw_input("Tamsayýyý giriniz:"))
            if tamsayi>=0:
                print "Tamsayýnýn mutlak deðeri:",tamsayi
            elif tamsayi<0:
                print "Tamsayýnýn mutlak deðeri:",tamsayi*-1

        elif sayi==3:
            ondaliksayi=float(raw_input("Ondalýk sayý giriniz:"))
            if ondaliksayi>=0:
                print"Ondalýk sayýnýn mutlak deðeri:",ondaliksayi
            elif tamsayi<0:
                print"Ondalýk sayýnýn mutlak deðeri:",ondaliksayi*-1
        else:
            break
        
mutlak_genel()        
              
        
        
        
