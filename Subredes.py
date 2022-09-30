import functions

subredesNecessarias = int(input("Insira a quantidade de subredes desejada: "))

while subredesNecessarias > 0:

    elevado = 1
    while ((2 ** elevado) - 2) < subredesNecessarias:
        elevado += 1

    binary = (functions.elevadoToBinary(elevado))
    decimalHost = (functions.binaryToDecimal(binary))

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