#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def dene(s):
    """
     >>>has_dashdash('distance--but')
     True
     >>>has_dashdash("several")
     False
     >>>has_dashdash("critters")
     False
     >>>has_dashdash("spoke--fancy")
     True
     >>>has_dashdash("yo-yo")
     False
    """ 

    count=0
    for i in s:
        if i=="-":
            count+=1
        else:
            pass
    if count==2:
        return True
    else:
        return False


    doctest.testmod()

