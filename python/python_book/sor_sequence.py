#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def sort_sequence(seq):
    """
    >>>sort_sequence([3,4,6,7,8,2])
    [2,3,4,6,7,8]
    >>>sort_sequence((3,4,6,7,8,2))
    (2,3,4,6,7,8)
    >>>sort_sequence("nothappy")
    'ahnoppty'
    """
 
    if type(seq)==type([]):
        lis=[]
        for i in range(len(seq)):
            bul=min(seq)
            lis.append(bul)
            seq.remove(bul)

    elif type(seq)==type(()):
        lis=[]
        seq=list(seq)
        for i in range(len(seq)):
            bul=min(seq)
            lis.append(bul)
            seq.remove(bul)
        lis=tuple(lis)

    elif type(seq)==type(""):
        seq=list(seq)
        lis=[]
        for i in range(len(seq)):
            bul=min(seq)
            lis.append(bul)
            seq.remove(bul)
        lis="".join(lis)    
        
    return lis

    doctest.testmod()

