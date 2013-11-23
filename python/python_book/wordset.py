#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def dene(wordlist):
    """
     >>>wordset(["now","is","time","is","now","is","ecmel"])
     ["now","is","time","ecmel"]
     >>>wordset(["I","a","a","is","a","is","I","am"])
     ["I","a","is","am"]
     >>>wordset(["or","a","am","is","are","be","but","am"])
     ["or","a","am","is","are","be","but"]
    """ 

    lis=[]
    first=wordlist[0]
    lis.append(first)
    for i in wordlist:
        if not i in lis:
            lis.append(i)
        else:
            pass
    return lis


    doctest.testmod()

            
