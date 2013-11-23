#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def count(sub,s):
    """
    >>>count("is,"mississippi")
    2
    >>>count("an","banana")
    2
    >>>count("nana","banana")
    1
    >>>count("nanan","banana")
    0
    """

    say=0
    while sub in s:
        bul=s.find(sub)
        s=s[:bul]+s[bul+len(sub):]
        say+=1
    return say

    doctest.testmod() 

