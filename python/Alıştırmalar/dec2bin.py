from Stack import Stack
def dec2bin(decNumber):

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber / 2

    binString = ""

    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
