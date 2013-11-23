from __future__ import division
secenek1="(1) toplama"
secenek2="(2) çýkarma"
secenek3="(3) çarpma"
secenek4="(4) bölme"

print secenek1
print secenek2
print secenek3
print secenek4

soru=raw_input("sorulacak sorunun numarasýný gir:")

if soru=="1":
    sayi1=input("toplama için ilk sayýyý gir:")
    print sayi1
    sayi2=input("toplama için ikinci sayýyý gir:")
    print sayi1,"+",sayi2,":",sayi1+sayi2
if soru=="2":
    sayi3=input("çýkarma için ilk sayýyý gir:")
    print sayi3
    sayi4=input("çýkarma için ikinci sayýyý gir:")
    print sayi3,"-",sayi4,":",sayi3-sayi4
if soru=="3":
    sayi5=input("çarpma için ilk sayýyý gir:")
    print sayi5
    sayi6=input("çarpma için ikinci sayýyý gir:")
    print sayi5,"*",sayi6,":",sayi5*sayi6
if soru=="4":
    sayi7=input("bölme için ilk sayýyý gir:")
    print sayi7
    sayi8=input("bölme için ikinci sayýyý gir:")
    print sayi7,"/",sayi8,":",sayi7/sayi8
