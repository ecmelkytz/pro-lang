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
   
    while letter in strng:
        for i in strng:
            if i==letter:
                bul=strng.index(i)
                strng=strng[:bul]+strng[bul+len(letter):]

    return strng

