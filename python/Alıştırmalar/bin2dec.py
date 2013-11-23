from Stack import Stack
def bin2dec(binNumber):

    remstack = Stack()
    index = 0
    while binNumber > 0 :
        rem = (binNumber%10) * pow(2,index)
        remstack.push(rem)
        binNumber = binNumber / 10
        index += 1
    decNumber = 0 

    while not remstack.isEmpty():
        decNumber = decNumber + remstack.pop()
        
    return str(decNumber)
        
