#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def insert_in_front(val,seq):
    """
    >>>insert_in_front(5,[1,3,4,6])
    [5,1,3,4,6]
    >>>insert_in_front(5,(1,3,4,6))
    (5,1,3,4,6)
    >>>insert_in_front("x","abc")
    'xabc'
    """

    if type(seq)==type([]):
        seq.insert(0,val)

    elif type(seq)==type(()):
        seq=(val,)+seq

    elif type(seq)==type(""):
        seq=val+seq

    return seq  

    doctest.testmod()

