import doctest

def ardisik_toplam(x):
    if x>0:
        t=0
        while x>0:
            t=t+x
            x=x-1
        print t
    else:
        print "lütfen tamsayı giriniz."

doctest.testmod()
