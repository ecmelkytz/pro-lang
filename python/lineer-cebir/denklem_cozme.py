print "ilk gireceginiz lineer denklem en cok bilinmeyen iceren olsun.or:x+2y-z=5"
say=0
sabit=[]
bilinmeyen=[]
matris=[]
while True:
    katsayi=[]
    denklem=raw_input("denklemi giriniz:")
    for i in range(len(denklem)):
        if not "0"<=denklem[i]<="9" and denklem[i]!="+" and denklem[i]!="-" and denklem[i]!="*" and denklem[i]!="=":
            bilinmeyen.append(denklem[i])
            say+=1
            if denklem.index(denklem[i])==0:
                katsayi.append(1)
            elif denklem[i-1]=="-":
                katsayi.append(-1)    
            elif denklem[i-1]=="+":
                katsayi.append(+1)
            elif "0"<=denklem[i-1]<="9":
                if denklem[i-2]=="+":
                    katsayi.append(int(denklem[i-1]))
                elif denklem[i-2]=="-":
                    katsayi.append(int(denklem[i-1])*(-1))
                else:
                    katsayi.append(int(denklem[i-1]))            
                
        elif denklem[i]=="=":
            i+=1
            sabit.append(int(denklem[i]))
            break
    break
matris.append(katsayi)
print katsayi

while True:
    uzun=0
    bil=[]
    kat=[]
    devam=raw_input("devam etmek istiyorsan e istemiyorsan h yaz:")
    if devam=="h":
        break
    else:
        say+=1
        denklem=raw_input("denklemi giriniz:")
        for i in range(len(denklem)):
            if not "0"<=denklem[i]<="9" and denklem[i]!="+" and denklem[i]!="-" and denklem[i]!="*" and denklem[i]!="=":
                bil.append(denklem[i])
                if bilinmeyen[uzun] in denklem[i]:
                    uzun+=1
                    if denklem.index(denklem[i])==0:
                        kat.append(1)
                    elif denklem[i-1]=="-":
                        kat.append(-1)
                    elif denklem[i-1]=="+":
                        kat.append(1)
                    elif "0"<=denklem[i-1]<="9":
                        if denklem[i-2]=="+":
                            kat.append(int(denklem[i-1]))
                        elif denklem[i-2]=="-":
                            kat.append(int(denklem[i-1])*(-1))                        
                        else:
                            kat.append(int(denklem[i-1]))
                else:
                    while bilinmeyen[uzun]!=denklem[i]:
                        uzun+=1
                        kat.append(0)
                    uzun+=1    
                    if denklem.index(denklem[i])==0:
                        kat.append(1)
                    elif denklem[i-1]=="-":
                        kat.append(-1)
                    elif denklem[i-1]=="+":
                        kat.append(1)
                    elif "0"<=denklem[i-1]<="9":
                        if denklem[i-2]=="+":
                            kat.append(int(denklem[i-1]))
                        elif denklem[i-2]=="-":
                            kat.append(int(denklem[i-1])*(-1))                        
                        else:
                            kat.append(int(denklem[i-1]))                   
           
            elif denklem[i]=="=":
                i+=1
                sabit.append(int(denklem[i]))
                ckatsayi=len(katsayi)
                ckat=len(kat)
                while ckatsayi!=ckat:
                    kat.append(0)
                    ckat+=1
                print kat
                matris.append(kat)
                break
       
print matris   
print sabit


