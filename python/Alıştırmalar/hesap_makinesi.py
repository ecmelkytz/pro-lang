from __future__ import division
secenek1="(1) toplama"
secenek2="(2) ��karma"
secenek3="(3) �arpma"
secenek4="(4) b�lme"

print secenek1
print secenek2
print secenek3
print secenek4

soru=raw_input("sorulacak sorunun numaras�n� gir:")

if soru=="1":
    sayi1=input("toplama i�in ilk say�y� gir:")
    print sayi1
    sayi2=input("toplama i�in ikinci say�y� gir:")
    print sayi1,"+",sayi2,":",sayi1+sayi2
if soru=="2":
    sayi3=input("��karma i�in ilk say�y� gir:")
    print sayi3
    sayi4=input("��karma i�in ikinci say�y� gir:")
    print sayi3,"-",sayi4,":",sayi3-sayi4
if soru=="3":
    sayi5=input("�arpma i�in ilk say�y� gir:")
    print sayi5
    sayi6=input("�arpma i�in ikinci say�y� gir:")
    print sayi5,"*",sayi6,":",sayi5*sayi6
if soru=="4":
    sayi7=input("b�lme i�in ilk say�y� gir:")
    print sayi7
    sayi8=input("b�lme i�in ikinci say�y� gir:")
    print sayi7,"/",sayi8,":",sayi7/sayi8
