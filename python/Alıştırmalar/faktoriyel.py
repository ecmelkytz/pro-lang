def faktoriyel_hesapla(sayi):
    while sayi:
        if(sayi==0 or sayi==1):
            return 1
        elif sayi<0:
            print "negatif sayıların faktöriyel hesaplaması yapılamaz."
            break
        else:
            return sayi*faktoriyel_hesapla(sayi-1)
        
        
