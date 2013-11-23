def dene(x):
    if len(str(x))==11 and type(x)==type(1):
        x=str(x)
        say1,say2,say3=0,0,0
        lis1,lis2,lis3=[],[],[]
        for i in range(0,10,2):
            lis1.append(x[i])
        for i in range(1,9,2):
            lis2.append(x[i])        
        for i in range(0,10):
            lis3.append(x[i])    
        for i in lis1:
            i=int(i)
            say1+=i
        for i in lis2:
            i=int(i)
            say2+=i
        for i in lis3:
            i=int(i)
            say3+=i    
        x=int(x)
        toplam=(say1*7)-(say2)
        islem=toplam%10
        islem=str(islem)
        son=x%10
        islem1=say3%10
        x=str(x)
    
        if islem==x[-2] and islem1==son:
            print ("TC kimlik numarası geçerlidir.")
        else:
            print ("TC kimlik numarası geçerli değildir.")
        
    else:
        print ("lütfen 11 basamaklı bir tamsayı giriniz!")
        
  
