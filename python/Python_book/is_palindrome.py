#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def is_palindrome(s):
    """
    >>>is_palindrome("abba")
    True
    >>>is_palindrome("abab")
    False
    >>>is_palindrome("tenet")
    True
    >>>is_palindrome("banana")
    False
    >>>is_palindrome("straw warts")
    True
    """
    
    def mirror(a):
        lis=[]
        for i in a:
            lis.insert(0,i)
        yaz="".join(lis)
        return yaz

    if s==mirror(s):
        return True
    else:
        return False

    doctest.testmod()

