#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def remove(sub,s):
    """
    >>>remove("an","banana")
    'bana'
    >>>remove("cyc","bicycle")
    'bile'
    >>>remove("iss","mississippi")
    'missippi'
    >>>remove("egg","bicycle")
    'bicycle'
    """

    if sub in s:
        bul=s.index(sub)
        s=s[:bul]+s[bul+len(sub):]
    return s

    doctest.testmod() 
