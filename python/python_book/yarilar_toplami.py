#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def yarilar_toplami(x):
    """
    >>>yarilar_toplami(2)
    1.5
    >>>yarilar_toplami(3)
    2.625
    >>>yarilar_toplami(5)
    4.84375
    >>>yarilar_toplami(7)
    6.890625
    >>>yarilar_toplami(0)
    Lütfen pozitif bir tamsayı giriniz.
    >>>yarilar_toplami(-4)
    Lütfen pozitif bir tamsayı giriniz.
    >>>yarilar_toplami(6.8)
    Lütfen pozitif bir tamsayı giriniz.
    """

    top=0
    if x>0:
        for i in range(x):
            bol=x/2
            x=bol
            if bol>0.1:
                top+=bol
            else:
                pass
        return top    

    else:
        print ("lütfen pozitif bir tamsayı giriniz.")

    doctest.testmod()

