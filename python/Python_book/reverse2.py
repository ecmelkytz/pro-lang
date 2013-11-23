#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def reverse2(x):
    """
    >>>reverse2([1,2,3,4,5])
    [5,4,3,2,1]
    >>>reverse2(("shoes","my","buckle",2,1))
    (1,2,"buckle","my","shoes")
    >>>reverse2("python")
    'nohtyp'
    """

    lis=[]
    if type(x)==type([]):
        for i in x:
            lis.insert(0,i)
        return lis

    elif type(x)==type(""):
        x=list(x)
        for i in x:
            lis.insert(0,i)    
        return "".join(lis)

    elif type(x)==type(()):
        x=list(x)
        for i in x:
            lis.insert(0,i)
        lis=tuple(lis)
        return lis 

    doctest.testmod()
