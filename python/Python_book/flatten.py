#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def flatten(x):
    """
    >>>flatten([2,9,[2,1,13,2],8,[2,6]])
    [2,9,2,1,13,2,8,2,6]
    >>>flatten([[9,[7,1,13,2],8],[2,6]])
    [9,7,1,13,2,8,2,6]
    >>>flatten([[5,[5,[1,5],5],5],[5,6]])
    [5,5,1,5,5,5,5,6]
    """

    ilk=x[0]
    if type(ilk)==type([]):
        ilk=ilk[0]
    lis=[]
    for i in x:
        if type(i)==type([]):
            yaz=dene(i)
            for a in yaz:
                lis.append(a)
        else:
            lis.append(i)
    return lis 

    doctest.testmod()

