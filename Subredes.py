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

subredesNecessarias = int(input("Insira a quantidade de subredes desejada: "))

while subredesNecessarias > 0:

    elevado = 1
    while ((2 ** elevado) - 2) < subredesNecessarias:
        elevado += 1

    binary = (elevadoToBinary(elevado))
    decimalHost = (binaryToDecimal(binary))

    primeiroEndereco = (256 - decimalHost)

    print("------------------------------------")
    print(f"Máscara a ser usada: 255.255.255.{decimalHost}")
    print("------------------------------------")

    for i in range(subredesNecessarias):
        print(f"Subrede número {i+1}:")
        print(f"ID:                 192.168.0.{(primeiroEndereco * (i+1))}")
        print(f"Primeiro Host:      192.168.0.{((primeiroEndereco * (i+1)) + 1)}")
        print(f"Último Host:        192.168.0.{((primeiroEndereco * (i+2)) - 2)}")
        print(f"Broadcast:          192.168.0.{((primeiroEndereco * (i+2)) - 1)}")
        print("------------------------------------")
    
    subredesNecessarias = int(input("Insira a quantidade de sub redes desejada, ou 0 para encerrar: "))

# TODO: Configurar o colorama
# TODO: Colocar numero maximo possivel de subredes
# TODO: Configurar IPS classe A e B