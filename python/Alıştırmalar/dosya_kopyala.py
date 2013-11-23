
def dosya_kopyala(kaynak,hedef):
    okunan=open(kaynak,'r')
    yazilan=open(hedef,'w')
    while True:
        metin=okunan.read(50)
        if metin=="":
            break
        yazilan.write(metin)
    okunan.close()
    yazilan.close()
    return
