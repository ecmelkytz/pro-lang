
from math import*

def kok_hesapla(a,b,c):
    d=b**2-4*a*c
    if d>0:
        w1=(-b+d**0.5)/2*a
        w2=(-b-d**0.5)/2*a
        print "Denklemin birinci k�k�:",w1
        print "Denklemin ikinci k�k�:",w2
    else:
        print "Denklemin ger�el k�k� bulunmamaktad�r."

kok_hesapla(1,-1,-6)       

