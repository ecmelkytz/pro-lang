import doctest

def kac_basamak(sayi):
    """
    >>>kac_basamak(67853)
    5
    >>>kac_basamak(600)
    3
    >>>kac_basamak(8)
    1
    >>>kac_basamak(-8)
    1
    """
    x=0
    while sayi:
        x+=1
        sayi/=1
    return x

kac_basamak(600)

doctest.testmod()
