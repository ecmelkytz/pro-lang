#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def num_digits(n):
    """
    >>>num_digits(13245)
    5
    >>>num_digits(0)
    1
    >>>num_digits(-13245)
    5
    """

    say=0
    if n<0:
        n=n*(-1)
    elif n==0:
        return 1
    
    while n:
        say+=1
        n/=10
    return say

    doctest.testmod()

