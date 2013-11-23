#!/usr/bin/env python
# -*- coding: utf8 -*-

import doctest
def wordcount(word,wordlist):
    """
     >>>wordcount("now",["now","is","time","is","now","is","is"])
     ["now",2]
     >>>wordcount("is",["now","is","time","is","now","is","the","is"])
     ["is",4]
     >>>wordcount("time",["now","is","time","is","now","is","is"])
     ["time",1]
     >>>wordcount("frog",["now","is","time","is","now","is","is"])
     ["frog",0]
    """ 

    lis=[]
    count=0
    for i in wordlist:
        if i==word:
            count+=1
        else:
            pass
    lis.append(word)
    lis.append(count)
    return lis


    doctest.testmod()
