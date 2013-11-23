class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n,pA,pB):
        LogicGate.__init__(self,n)

        self.pinA = pA
        self.pinB = pB

    def getPinA(self):
        if self.pinA == None:
            return self.pinA
        #else:
         #   return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return self.pinB 
       # else:
        #    return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print "Cannot Connect: NO EMPTY PINS"

class AndGate(BinaryGate):

    def __init__(self,n,pA=None,pB=None):
        BinaryGate.__init__(self,n,pA,pB)

    def performGateLogic(self):

        a = self.pinA
        b = self.pinB
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n,pA=None,pB=None):
        BinaryGate.__init__(self,n,pA,pB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0
class XorGate(BinaryGate):

    def __init__(self,n,pA=None,pB=None):
        BinaryGate.__init__(self,n,pA,pB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1

class NorGate(BinaryGate):

    def __init__(self,n,pA=None,pB=None):
        BinaryGate.__init__(self,n,pA,pB)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 0
        else:
            return 1



class NandGate(BinaryGate):

    def __init__(self,n,pA=None,pB=None):
        BinaryGate.__init__(self,n,pA,pB)

    def performGateLogic(self):

        a = self.pinA
        b = self.pinB
        if a==1 and b==1:
            return 0
        else:
            return 1


class UnaryGate(LogicGate):

    def __init__(self,n,p):
        LogicGate.__init__(self,n)

        self.pin = p

    def getPin(self):
        if self.pin == None:
            return self.pin
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print "Cannot Connect: NO EMPTY PINS"

class NotGate(UnaryGate):

    def __init__(self,n,p=None):
        UnaryGate.__init__(self,n,p)

    def performGateLogic(self):

        if self.getPin():
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
        

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

# Test
g1 = AndGate("G1",1,0)
g2 = AndGate("G2",1,0)
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print g4.getOutput()
