#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def make_empty(x):
    """
    >>>make_empty([1,2,3,4])
    []
    >>>make_empty(("a","b","c"))
    ()
    >>>make_empty("no, not me!")
    ''
    """

    if type(x)==type([]):
        while 0<len(x):
            for i in x:
                x.remove(i)

    elif type(x)==type(()):
        x=list(x)
        while 0<len(x):
            for i in x:
                x.remove(i)
        x=tuple(x)

    elif type(x)==type(""):
        x=x.split()
        while 0<len(x):
            for i in x:
                x.remove(i)
        x="".join(x)       
 
    return x 

    doctest.testmod()

