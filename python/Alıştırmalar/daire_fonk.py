from math import*
def daire_fonk(x):
    cevre=2*pi*x
    alan=pi*x**2
    if x>0:
        print "Dairenin �evresi",cevre,"birimdir."
        print "Dairenin alan�",alan,"birim karedir."
    else:
        print "Yar��ap s�f�rdan k���k olamaz."

daire_fonk(10)
daire_fonk(-7)
