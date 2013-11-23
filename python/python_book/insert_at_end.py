#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def insert_at_end(val,seq):
    """
    >>>insert_at_end(5,[1,3,4,6])
    [1,3,4,6,5]
    >>>insert_at_end('x','abc')
    'abcx'
    >>>insert_at_end(5,(1,3,4,6))
    (1,3,4,6,5)
    """

    if type(seq)==type([]):
        seq.append(val)

    elif type(seq)==type(""):
        seq+=val

    elif type(seq)==type(()):
        seq+=(val,)


    return seq

    doctest.testmod()
