import time
sayi=raw_input("say� giriniz or=a/b:")
a,b=sayi.split("/")
a,b=int(a),int(b)
start=time.clock()
obeb=1                 #girilen sayilarin ebobunu hesapladim.          
if a<b:                #sayilari eboblarina b�lerek aralarinda asal hale getirdim.
    kucuk=a
    buyuk=b
else:
    kucuk=b
    buyuk=a
for i in range(1,kucuk+1):
    if a/i*i==a and b/i*i==b:
        obeb=obeb*i
        a=a/i
        b=b/i
okek=obeb*a*b


liste=[]                    #2 tane liste olusturdum.
yenilis=[]
                                 #mesela 2/3 seklinde girdigim sayiyi 1/3+1/3 seklinde payi 1 olarak ayirdim.
for i in range(a):               #a(pay) sayisi kadar b(payda)'y� bu listeye ekledim.Yani sadece payday� ekliyorum.
    liste.append(b)
                                
if a!=1:                        #e�er a=1 de�ilse bir d�ng�ye girdim.
    yenilis.append(liste[0])       #ilk listedeki 1. say�y� di�er listeye att�m.��nk� d�ng�y� 0. indisten ba�latmad�m.    
    for i in range(pow(2,a-1)-1):    
        z,y=liste[i]+1,(liste[i]*(liste[i]+1))  #1/x=1/(x+1)+1/(x(x+1)) mant���n� kullanarak sadece paydalarla i� yap�yorum.
        yenilis.append(z)                       #yani x=(x+1)+x(x+1) i�lemini yap�yorum.
        yenilis.append(y)                       #ve bunlar� di�er listeye ekliyorum.
        liste=yenilis                           #ilk listeyi di�er listeye e�itliyorum ki d�ng� istenmedik yerde bitmesin.

elif a==1:                      #e�er a=1 ise bu d�ng�ye girece�im.��nk� bu kesirler i�in �zel durumlar var.
    if b%2==0:                  #payda e�er �ift ise 2n=n(3+6) denklemini uyguluyorum.
        bol=b/2                 #burada 3+6 ile ifade edilen yer asl�nda 1/3+1/6 (bizden istenen bu)
        x,y=(bol*3),(bol*6)
        yenilis.append(x)
        yenilis.append(y)
    elif b%2==1:            #payda e�er tek ise p=p(2+3+6)
        x,y,z=b*2,b*3,b*6
        yenilis.append(x)     #bu say�lar� ikinci listeye ekliyoruz.
        yenilis.append(y)
        yenilis.append(z)
end=time.clock()
print end
print yenilis
    
        
        
    
    
    
    
