def mutlak_genel():
    while True:
        sayi=input("karma��k say�lar i�in 1,tamsay�lar i�in 2"\
                   "ondal�k say�lar i�in 3,��kmak i�in 4 giriniz:")
        if sayi==1:
            a=int(raw_input("Ger�el k�sm� giriniz:"))
            b=int(raw_input("Sanal k�sm� giriniz:"))
            z=float((a**2+b**2)**0.5)
            print "Karma��k say�n�n mutlak de�eri:",z
        
        elif sayi==2:
            tamsayi=int(raw_input("Tamsay�y� giriniz:"))
            if tamsayi>=0:
                print "Tamsay�n�n mutlak de�eri:",tamsayi
            elif tamsayi<0:
                print "Tamsay�n�n mutlak de�eri:",tamsayi*-1

        elif sayi==3:
            ondaliksayi=float(raw_input("Ondal�k say� giriniz:"))
            if ondaliksayi>=0:
                print"Ondal�k say�n�n mutlak de�eri:",ondaliksayi
            elif tamsayi<0:
                print"Ondal�k say�n�n mutlak de�eri:",ondaliksayi*-1
        else:
            break
        
mutlak_genel()        
              
        
        
        
