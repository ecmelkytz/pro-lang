#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def remove_val(a,b):
    """
    >>>remove_val(11,[1,7,11,9,10])
    [1,7,11,10]
    >>>remove_val(15,(1,15,11,4,9))
    (1,11,4,9)
    """

    if type(b)==type([]):
       lis=[]
       for i in b:
           if i!=a:
               lis.append(i)
       return lis        

    elif type(b)==type(()):
        tup=()
        for i in b:
            if i!=a:
                tup+=(i,)

        return tup

    doctest.testmod()
