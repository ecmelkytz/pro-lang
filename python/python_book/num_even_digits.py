#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def num_even_digits(n):
    """
    >>>num_even_digits(123456)
    3
    >>>num_even_digits(2468)
    4
    >>>num_even_digits(1357)
    0 
    >>>num_even_digits(2)
    1
    >>>num_even_digits(20)
    2
    """

    n=str(n)
    x=0
    for i in n:
        i=int(i)
        if i%2==0:
            x+=1
        else:
            pass
    return x 

    doctest.testmod()

