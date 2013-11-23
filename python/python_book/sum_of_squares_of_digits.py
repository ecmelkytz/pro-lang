#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def sum_of_squares_of_digits(n):
    """
    >>>sum_of_squares_of_digits(1)
    1
    >>>sum_of_squares_of_digits(9)
    81
    >>>sum_of_squares_of_digits(11)
    2
    >>>sum_of_squares_of_digits(12)
    6
    >>>sum_of_squares_of_digits(987)
    194
    """

    n=str(n)
    x=0
    for i in n:
        i=int(i)
        x+=i**2
    return x
  
    doctest.testmod()
  
