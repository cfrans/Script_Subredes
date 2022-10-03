import functions
import sys
from colorama import Back, Fore, Style, init
init() # inicializa as cores

print("------------------------------------")
print("------Subredes by CFRANS 2022-------")
print("------------------------------------")
print("1 - Descobrir a máscara e os ranges a partir da quantidade necessária de subredes.")
print("0 - Encerrar.")

opcaoCorreta = False
while opcaoCorreta == False:
    opcao = input("Selecione a opção desejada: ")
    try:
        string_int = int(opcao)    
    except ValueError:
        print((Back.RED) + (Fore.WHITE))
        print("Informe somente o número, sem letras.")
        print(Style.RESET_ALL)
    if int(opcao) > 1 or int(opcao) < 0:
        print("Opção incorreta.")
    else:
        opcaoCorreta = True

if int(opcao) == 0:
    sys.exit(0)
elif int(opcao) == 1:
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