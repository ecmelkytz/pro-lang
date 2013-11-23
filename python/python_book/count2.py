#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def count2(x,y):
    """
    >>>count2(5,(1,5,3,7,5,8,5))
    3
    >>>count2("s","mississippi")
    4
    >>>count2((1,2),[1,5,(1,2),7,(1,2),8,5])
    2
    """

    say=0
    for i in y:
        if i==x:
            say+=1
    return say 

    doctest.testmod()

