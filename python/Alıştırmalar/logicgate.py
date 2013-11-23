class LogicGate:
    def __init__(self,n):
        self.label=n
        self.output=None

    def getlabel(self):
        return self.label

    def getOutput(self):
        self.output=self.performGateLogic()
        return self.output
class BinaryGate(LogicGate):
    def __init__(self ,n):
        LogicGate.__init__(self,n)

        self.pinA=None
        self.pinB=None

    def getPinA(self):
        if self.pinA==None:
            return input("Enter Pin A input for gate "+\
                         self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
         if self.pinB==None:
            return input("Enter Pin B input for gate "+\
                         self.getLabel()+"-->")
         else:
            return self.pinA.getFrom().getOutput()

    def setNexPin(self,source):
        if self.pinA==None:
            self.pinA==source
        else:
            if self.pinB==None:
                self.pinB==source
            else:
                print "Cannot Connect: NO EMPTY PINS"
class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinA()
        if a==1 and b==1:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinA()
        if a==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin=None

    def getPin(self):
        if self.pin==None:
            return input("Enter Pin input for gete"+\
                         self.getLabel()+"-->")
        else:
            print "Cannot Connect :NO EMPTY PINS"

class NotGate(UnaryGate):
        def __init__(self, n):
            UnaryGate.__init__(self,n)

        def performGateLogic(self):
            if self.getPin():
                return 0
            else:
                return 1

class Connector:
    def __init__(self,fgate,tgate):
        self.fromgate=fgate
        self.togate=tgate


        tgate.setNexPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate
    
    
    
