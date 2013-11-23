#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def extract_words(s):
    """
    >>>extract_words('Now is the time! "Now", is the time? Yes, now.')
    ['now','is','the','time','now','is','the','time','yes','now']
    >>>extract_words('she tried to curtsey as she spoke-- fancy')
    ['she','tried','to','curtsey','as','she','spoke','fancy']
    """
    bos=""
    for i in s:
        if i==i.isalpha() or i.isspace() or i.isalnum():
            bos+=i
        else:
            pass
    for  i in bos:
        if i==i.upper():
            bul=bos.index(i)
            bos=bos[:bul]+i.lower()+bos[bul+len(i):]

    return bos.split()

    doctest.testmod()

