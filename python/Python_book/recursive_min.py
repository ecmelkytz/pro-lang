#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def recursive_min(x):
    """
    >>>recursive_min([2,[[100,1],90],[10,13],8,6])
    1
    >>>recursive_min([2,[[13,-7],90],[1,100],8,6])
    -7
    >>>recursive_min([[[-13,7],90],2,[1,100],8,6])
    -13
    """

    ilk=x[0]
    while type(ilk)==type([]):
        ilk=ilk[0]
    for i in x:
        if type(i)==type([]):
            bul=dene(i)
            if ilk>bul:
                ilk=bul
        else:
            if ilk>i:
                ilk=i
    return ilk   

    doctest.testmod()
