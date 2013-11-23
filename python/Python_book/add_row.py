#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def add_row(matrix):
    """
    >>>m=[[0,0],[0,0]]
    >>>add_row(m)
    [[0,0],[0,0],[0,0]]
    >>>n=[[3,2,5],[1,4,7]]
    >>>add_row(n)
    [[3,2,5],[1,4,7],[0,0,0]]
    >>>n
    [[3,2,5],[1,4,7]]
    """ 
    lis=[]
    long=len(matrix[0])
    carp=[0]*long
    lis.extend(matrix)
    lis.append(carp)
    return lis

    doctest.testmod()

