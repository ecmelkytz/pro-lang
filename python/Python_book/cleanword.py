#!/usr/bin/env python
# -*- coding: utf8 -*-

def cleanword(word):
    """
     >>>cleanword('what?')
     'what'
     >>>cleanword('"now!"')
     'now'
     >>>cleanword('?+="word!,@$()"')
     'word'
    """ 
    bos=""
    for i in word:
        if i==i.isalnum() or i.isalpha() or i.isdigit():
            bos+=i
        else:
            pass
    return bos    


    if __name__=="__main__":
        import doctest
        doctest.testmod()
