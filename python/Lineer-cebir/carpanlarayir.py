a = input("sayi giriniz:")
liste = [ ]
bolen = 2

for i in range(1,a):

    while a % bolen == 0:
        if a % bolen == 0:
            liste.append(bolen)
            c = a / bolen
            d = c
            a = d

    bolen += 1
print liste
