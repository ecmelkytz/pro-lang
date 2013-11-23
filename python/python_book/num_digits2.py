#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def num_digits2(n):
    """
    >>>num_digits2(13245)
    5
    >>>num_digits2(0)
    1
    >>>num_digits2(-13245)
    5
    """
    n=str(n)
    bos=""
    for i in n:
        if i!="-":
            bos+=i
        else:
            pass
    return len(bos)    

    doctest.testmod()

    
