def fib(n):
    if n>=0:
        x,y=0,1
        b=1
        while True:
            x,y=y,x+y
            b+=1
            if b<=n:
                continue
            else:
                return x
    else:
        print "pozitif sayý gir."
