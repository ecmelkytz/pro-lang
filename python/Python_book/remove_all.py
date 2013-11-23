#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def remove_all(sub,s):
    """
    >>>remove("an","banana")
    'ba'
    >>>remove("cyc","bicycle")
    'bile'
    >>>remove("iss","mississippi")
    'mippi'
    >>>remove("egg","bicycle")
    'bicycle'
    """

    while sub in s:
        bul=s.index(sub)
        s=s[:bul]+s[bul+len(sub):]
    return s 

    doctest.testmod()
   
