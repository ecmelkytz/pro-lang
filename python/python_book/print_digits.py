#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def print_digits(n):
    """
    >>>print_digits(13789)
    9 8 7 3 1
    >>>print_digits(39874613)
    3 1 6 4 7 8 9 3
    >>>print_digits(213141)
    1 4 1 3 1 2
    """

    n=str(n)
    lis=[]
    say=0
    for i in n:
        say+=1
        lis.insert(0,i)
        if say<=len(n)-1:
            lis.insert(0," ")
    print ("".join(lis))

    doctest.testmod()

