import time
sayi=raw_input("sayý giriniz or=a/b:")
a,b=sayi.split("/")
a,b=int(a),int(b)
start=time.clock()
obeb=1                 #girilen sayilarin ebobunu hesapladim.          
if a<b:                #sayilari eboblarina bölerek aralarinda asal hale getirdim.
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
for i in range(a):               #a(pay) sayisi kadar b(payda)'yý bu listeye ekledim.Yani sadece paydayý ekliyorum.
    liste.append(b)
                                
if a!=1:                        #eðer a=1 deðilse bir döngüye girdim.
    yenilis.append(liste[0])       #ilk listedeki 1. sayýyý diðer listeye attým.çünkü döngüyü 0. indisten baþlatmadým.    
    for i in range(pow(2,a-1)-1):    
        z,y=liste[i]+1,(liste[i]*(liste[i]+1))  #1/x=1/(x+1)+1/(x(x+1)) mantýðýný kullanarak sadece paydalarla iþ yapýyorum.
        yenilis.append(z)                       #yani x=(x+1)+x(x+1) iþlemini yapýyorum.
        yenilis.append(y)                       #ve bunlarý diðer listeye ekliyorum.
        liste=yenilis                           #ilk listeyi diðer listeye eþitliyorum ki döngü istenmedik yerde bitmesin.

elif a==1:                      #eðer a=1 ise bu döngüye gireceðim.çünkü bu kesirler için özel durumlar var.
    if b%2==0:                  #payda eðer çift ise 2n=n(3+6) denklemini uyguluyorum.
        bol=b/2                 #burada 3+6 ile ifade edilen yer aslýnda 1/3+1/6 (bizden istenen bu)
        x,y=(bol*3),(bol*6)
        yenilis.append(x)
        yenilis.append(y)
    elif b%2==1:            #payda eðer tek ise p=p(2+3+6)
        x,y,z=b*2,b*3,b*6
        yenilis.append(x)     #bu sayýlarý ikinci listeye ekliyoruz.
        yenilis.append(y)
        yenilis.append(z)
end=time.clock()
print end
print yenilis
    
        
        
    
    
    
    
