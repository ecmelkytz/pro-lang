#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def yarilar_toplami(x):
    """
    >>>yarilar_toplami('3-5-7-9')
    dizi anahtari:36
    >>>yarilar_toplami('3-10-7-5')
    dizi anahtari:36
    >>>yarilar_toplami('3-10-7')
    dizi anahtari:42
    >>>yarilar_toplami('7-3-10')
    dizi anahtari:42
    """

    lis=[]
    lis2=[]
    say=0
    ayir=x.split("-")

    for i in ayir:
        i=int(i)
        lis.append(i)

    if lis!=lis.sort():
        for i in range(len(lis)):
            bul=min(lis)
            lis2.append(bul)
            lis.remove(bul)
    else:
        pass

    uzun=len(lis2)
    for i in lis2:
        i=int(i)
        say+=i
    a=int(say/uzun)
   
    if uzun%2==0:
        bol=int(uzun/2)
        bol1=int(bol-1)
        bul=int(lis2[bol])
        bul1=int(lis2[bol1])
        toplam=int(bul1+bul)
        sonuc=int(toplam/2)
        b=sonuc
    
    else:
        bol=int(uzun/2)
        bul=int(lis2[bol])
        b=bul    

    
    print ("dizi anahtari:",a*b)

    doctest.testmod()

