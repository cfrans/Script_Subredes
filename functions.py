def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)   

def decBitsToBinary(n):
    if n == 1:
        binary = 10000000
    elif n == 2:
        binary = 11000000
    elif n == 3:
        binary = 11100000
    elif n == 4:
        binary = 11110000
    elif n == 5:
        binary = 11111000
    elif n == 6:
        binary = 11111100
    elif n == 7:
        binary = 11111110
    elif n == 8:
        binary = 11111111
    return(binary)
