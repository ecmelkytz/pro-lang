from Stack import Stack

def base2dec(strNumber,base):

    digits = "123456789ABCDEF"

    remstack = Stack()
    index = 0
    
    while strNumber > 0:
        rem = (strNumber % 10) * pow(base,index)
        strNumber /= 10
        remstack.push(rem)
        index += 1
    decNumber = 0
    while not remstack.isEmpty():
        decNumber = decNumber + remstack.pop()
        
    return str(decNumber)
    
        
        
