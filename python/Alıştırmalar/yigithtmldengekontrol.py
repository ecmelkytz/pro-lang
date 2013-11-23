class stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self,n=None):
        if n==None:
             return self.items.pop()
        else:
             return self.items.pop(n)
    def peek(self,n=None):
        if n==None:
             return self.items[len(self.items)-1]
        else:
             return self.items[n]
    def size(self):
        return len(self.items)

def htmlChecker(list):
        s=stack()
        k=stack()
        balanced=True
        index=0
        ac=0
        kapa=0

        while index<len(list):
            symbol=list[index]
            if symbol[0]!='/':
                s.push(symbol)
                ac=ac+1
            else:
                kapa=kapa+1
                if s.isEmpty()==False:
                    top=s.pop()
                    if not matches(top,symbol):
                       k.push(symbol)
                       s.push(top)
                       balanced=False
                else:
                    k.push(symbol)
                    balanced=False
            index=index+1
        if balanced and s.isEmpty():
            print "html kodlarnz dengeli"
        else:
            for i in range (0,s.size()):
                    for j in range (0,k.size()):
                        if '/'+s.peek(0)==k.peek():
                            s.pop(0)
                            k.pop()
            if ac==kapa and s.size()==0 and k.size()==0:
                print "eksik kod yok ama yanls yerlerde duruyolar"
            else:
                opens=['html','title','body','h1','i']
                closers=['/html','/title','/body','/h1','/i']
                
                for i in range(0,k.size()):
                    for j in range (0,len(opens)):
                        if k.items[i]==closers[j]:
                            print opens[j]+"  kodunuz eksik"                   
            
                for i in range(0,s.size()):
                   for j in range (0,len(closers)):
                        if s.items[i]==opens[j]:
                            print closers[j]+"  kodunuz eksik" 
def matches(open,close):
        opens=['html','title','body','h1','b','i']
        closers=['/html','/title','/body','/h1','/b','/i']
        return opens.index(open)==closers.index(close)
        
htmlChecker(['html','title','/title','h1','body','i','/i','/body','/h1','/html'])

htmlChecker(['html','title','/title','h1','i','/i','/body','/h1','/html'])

htmlChecker(['html','title','/title','h1','body','i','/body','/h1','/html'])

htmlChecker(['html','/title','title','h1','body','i','/i','/body','/h1','/html'])
