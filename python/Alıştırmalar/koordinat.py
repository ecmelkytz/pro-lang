
def hangi_bolge(x,y):
    if x>0 and y>0:
        print "koordinat düzleminde 1.bölgededir."
    elif x<0 and y>0:
        print "koordinat düzleminde 2. bölgededir."
    elif x<0 and y<0:
        print "koordinat düzleminde 3. bölgededir"
    elif x>0 and y<0:
        print "koordinat düzleminde 4.bölgededir."
hangi_bolge(5,-9)        
