#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def mirror(s):
    """
    >>>mirror("good")
    'gooddoog'
    >>>mirror("yes")
    'yessey'
    >>>mirror("a")
    'aa'
    """

    lis=[]
    for i in s:
	lis.insert(0,i)
    write="".join(lis)
    return s+write
    
    doctest.testmod()
