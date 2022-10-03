from colorama import Fore


def instaladorDependencias():
    import subprocess
    import sys
    print("--------------------------------------------------")
    print("A biblioteca Colorama será instalada.")
    input("Pressione enter para continuar")

    print("--------------------------------------------------")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
    'colorama'])
    print("--------------------------------------------------")
    print("Colorama instalado com sucesso.")
    print("--------------------------------------------------")

    print("Inicie novamente o script")
    sys.exit(0)

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

def exibirSubredes(i, primeiroEndereco):
    print(f"{Fore.LIGHTBLACK_EX}Subrede número {i+1}:")
    print(f"{Fore.LIGHTGREEN_EX}ID:                 {Fore.LIGHTCYAN_EX}192.168.0.{(primeiroEndereco * (i+1))}")
    print(f"{Fore.LIGHTGREEN_EX}Primeiro Host:      {Fore.CYAN}192.168.0.{((primeiroEndereco * (i+1)) + 1)}")
    print(f"{Fore.LIGHTGREEN_EX}Último Host:        {Fore.LIGHTBLUE_EX}192.168.0.{((primeiroEndereco * (i+2)) - 2)}")
    print(f"{Fore.LIGHTGREEN_EX}Broadcast:          {Fore.BLUE}192.168.0.{((primeiroEndereco * (i+2)) - 1)}")
    print("------------------------------------")