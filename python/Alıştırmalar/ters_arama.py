sehirler={'samsun':'karad.','antalya':'akd.','tokat':'karad.','manisa':'ege'}
def ters_arama(sehirler,deger):
    sehirler=dict()
    a=sehirler.values()
    x=0
    if deger not in a:
        print "indeks bulunamadı."
    else:
        if deger==sehirler[deger]:
            print sehirler[deger]
            x+=1
        else:
            pass



