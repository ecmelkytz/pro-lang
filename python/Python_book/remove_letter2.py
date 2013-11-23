#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def remove_letter(letter,strng):
    """
    >>>remove_letter("a","apple")
    'pple'
    >>>remove_letter("a","banana")
    'bnn'
    >>>remove_letter("z","banana")
    'banana'
    >>>remove_letter("i","mississippi")
    'msssspp'
    """

    lis=[]
    for i in strng:
        if i!=letter:
            lis.append(i)
        else:
            pass
    return "".join(lis) 
    
    doctest.testmod()
