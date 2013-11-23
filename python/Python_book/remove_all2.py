#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def remove_all2(a,b):
    """
    >>>remove_all(11,[1,7,11,9,11,10,2,11])
    [1,7,9,10,2]
    >>>remove_all("i","mississippi")
    'msssspp'
    """

    if type(b)==type([]):
        while a in b:
            bul=b.index(a)
            b.remove(b[bul])
        
    elif type(b)==type(""):
        while a in b:
            bul=b.index(a)
            b=b[:bul]+b[bul+len(a):]
            
    return b  

    doctest.testmod()

