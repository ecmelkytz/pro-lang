a=input("a sayisini gir:")
b=input("b sayisini gir:")
ebob=1                           
if a<b:         
    k=a
    b=b
else:
    k=b
    b=a

for i in range(1,k+1):
    if a/i*i==a and b/i*i==b:
        ebob=ebob*i
        a=a/i
        b=b/i
ekok=ebob*a*b

if ebob!=1:       
    say=0
    liste = [ ]
    x=a
    while say!=2:
        bolen=2
        for i in range(0,x):

            while x % bolen == 0:
                if x % bolen == 0:
                    liste.append(bolen)
                    c = x / bolen
                    d = c
                    x = d
                    
            bolen += 1
        say+=1    
        x=b

else:            
    say=0
    liste = [ ]
    x=a
    while say!=2:
        bolen=2
        for i in range(0,x):
            while x % bolen == 0:
                if x % bolen == 0:
                    liste.append(bolen)
                    c = x / bolen
                    d = c
                    x = d
                
            bolen += 1
        say+=1    
        x=b    


yenilis=[]
ikinci=[]
uc=[]

for i in range(len(liste)):
    for z in range(i+1,len(liste)):
        yenilis.append(liste[i]*liste[z])
            
for i in range(len(liste)):
    for z in range(len(yenilis)):
        ikinci.append(liste[i]*yenilis[z])

for i in range(len(liste)):
    for z in range(len(ikinci)):
        uc.append(liste[i]*ikinci[z])
      
ikinci=list(set(ikinci))
yenilis=list(set(yenilis))
uc=list(set(uc))
son=ikinci+yenilis+liste+uc
son.sort()
if a!=1:
    for i in range(len(son)):
        z=(b*son[i])/((a*son[i])-b)
        if z in son and z!=son[i]:
            print "a:",z,"b:",son[i]
            break
        else:
            continue
elif a==1:
    for i in range(len(son)):
        for z in range(i+1,len(son)):
            y=(b*son[i]*son[z])/((a*son[i]*son[z])-(b*son[z])-(b*son[i]))
            if y in son and a!=son[i] and a!=son[z]:
                print "a:",y,"b:",i,"c:",z
                break
            else:
                if son[i]==son[-1]:
                    print "bulunamadı."
    
    
  

