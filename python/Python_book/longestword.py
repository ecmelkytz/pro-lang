#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def longestword(wordset):
    """
     >>>longestword(["a","apple","pear","grape"])
     5
     >>>longestword(["a","am","I","be"])
     2
     >>>longestword(["ecmel","kaytazoglu"])
     10
    """

    lis=[]
    for i in wordset:
        lis.append(len(i))
    find_max=max(lis)   
    return find_max

    dostest.testmod()
