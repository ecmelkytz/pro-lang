#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def replace(s,old,new):
    """
    >>>replace("mississippi","i","I")
    'mIssIssIppI'
    >>>s='I love spom! spom is my favorite food.'
    >>>replace(s,"om","am")
    'I love spam! spam is my favorite food.'
    """

    ayir=s.split()
    while old in s:
        bul=s.index(old)
        s=s[:bul]+new+s[bul+len(old):]
    return "".join(s)

    doctest.testmod()

