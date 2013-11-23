#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def reverse(s):
    """
    >>>reverse('happy')
    'yppah'
    >>>reverse('Python')
    'nohtyP'
    >>>reverse('')
    ''
    >>>reverse('P')
    'P'
    """

    if type(a)==type([]):
        lis=[]
        for i in a:
            lis.insert(0,i)
        return lis

    elif type(a)==type(()):
        a=list(a)
        lis=[]
        for i in a:
            lis.insert(0,i)
        return tuple(lis)

    elif type(a)==type(""):
        a=a[::-1]
        return a

    doctest.testmod()
