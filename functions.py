def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)   

def decimalToBinary(n):
    # converting decimal to binary
    # and removing the prefix(0b)
    return bin(n).replace("0b", "")

def decBitsToBinary(n):
    if n == 1:
        bin = 10000000
    elif n == 2:
        bin = 11000000
    elif n == 3:
        bin = 11100000
    elif n == 4:
        bin = 11110000
    elif n == 5:
        bin = 11111000
    elif n == 6:
        bin = 11111100
    elif n == 7:
        bin = 11111110
    elif n == 8:
        bin = 11111111
    return(bin)

def binaryToElevado(n):
    if n == 10000000:
        elevado = 1
    elif n == 11000000:
        elevado = 2
    elif n == 11100000:
        elevado = 3
    elif n == 11110000:
        elevado = 4
    elif n == 11111000:
        elevado = 5
    elif n == 11111100:
        elevado = 6
    elif n == 11111110:
        elevado = 7
    elif n == 11111111:
        elevado = 8
    return(elevado)