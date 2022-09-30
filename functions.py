def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)   

def elevadoToBinary(elevado):
    if elevado == 1:
        binary = 10000000
    elif elevado == 2:
        binary = 11000000
    elif elevado == 3:
        binary = 11100000
    elif elevado == 4:
        binary = 11110000
    elif elevado == 5:
        binary = 11111000
    elif elevado == 6:
        binary = 11111100
    elif elevado == 7:
        binary = 11111110
    elif elevado == 8:
        binary = 11111111
    return(binary)
