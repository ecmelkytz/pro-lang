#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def add_list(a,b):
    """
     >>>dene([1,1],[1,1])
     [2,2]
     >>>dene([1,2],[1,4])
     [2,6]
     >>>dene([1,2,1],[1,4,3])
     [2,6,4]
    """
    lis=[]
    for i in range(len(a)):
        bul=a[i]+b[i]
        lis.append(bul)
    return lis    

    doctest.testmod()
