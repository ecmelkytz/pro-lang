from math import*
def daire_fonk(x):
    cevre=2*pi*x
    alan=pi*x**2
    if x>0:
        print "Dairenin çevresi",cevre,"birimdir."
        print "Dairenin alaný",alan,"birim karedir."
    else:
        print "Yarýçap sýfýrdan küçük olamaz."

daire_fonk(10)
daire_fonk(-7)
