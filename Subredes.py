import functions
import sys
try:
    from colorama import Back, Fore, Style, init
except ModuleNotFoundError:
        print('O módulo Colorama não foi encontrado. Iniciando o instalador de dependências...')
        functions.instaladorDependencias()

init() # inicializa as cores

print(f"{Fore.GREEN}------------------------------------")
print(f"{Fore.YELLOW}------Subredes by CFRANS 2022-------")
print(f"{Fore.LIGHTBLACK_EX}(Momentâneamente funcionando somente com IP Classe C)")
print(f"{Fore.GREEN}------------------------------------")
print(Fore.LIGHTBLUE_EX)
print("1 - Descobrir a máscara e os ranges a partir da quantidade necessária de subredes.")
print("2 - Descobrir as subredes a partir da máscara.")
print("3 - Transformar máscara CIDR.")
print(f"{Fore.LIGHTRED_EX}0 - Encerrar.{Fore.WHITE}")

opcaoCorreta = False
while opcaoCorreta == False:
    opcao = input("Selecione a opção desejada: ")
    try:
        string_int = int(opcao)    
    except ValueError:
        print((Back.RED) + (Fore.WHITE))
        print("Informe somente o número, sem letras.")
        print(Style.RESET_ALL)
    if int(opcao) > 3 or int(opcao) < 0:
        print("Opção incorreta.")
    else:
        opcaoCorreta = True

if int(opcao) == 0:
    sys.exit(0)

# 1 - Descobrir a máscara e os ranges a partir da quantidade necessária de subredes
elif int(opcao) == 1:
    subredesNecessarias = int(input("Insira a quantidade de subredes desejada: "))

    while subredesNecessarias > 0:

        elevado = 1
        while ((2 ** elevado) - 2) < subredesNecessarias:
            elevado += 1

        binary = (functions.decBitsToBinary(elevado))
        decimalHost = (functions.binaryToDecimal(binary))

        primeiroEndereco = (256 - decimalHost)

        print("------------------------------------")
        print(f"Máscara a ser usada: 255.255.255.{decimalHost}")
        print("------------------------------------")

        for i in range(subredesNecessarias):
            functions.exibirSubredes(i, primeiroEndereco)
        
        print(Fore.WHITE)
        subredesNecessarias = int(input("Insira a quantidade de sub redes desejada, ou 0 para encerrar: "))

# 2 - Descobrir as subredes a partir da máscara
elif int(opcao) == 2:
    mascara = int(input("Insira a máscara desejada: 255.255.255."))
    binary = int((functions.decimalToBinary(mascara)))
    elevado = (functions.binaryToElevado(binary))
    subredesPossiveis = (2 ** elevado) - 2
    primeiroEndereco = (256 - mascara)

    print(f"Quantidade de subredes possíveis: {subredesPossiveis}.")
    print("Informe a quantidade desejada para exibir os detalhes")
    opcao = input("Ou digite T para ver todas: ")

    if opcao == "T" or opcao == "t":
        for i in range(subredesPossiveis):
            functions.exibirSubredes(i, primeiroEndereco)
    elif int(opcao) > subredesPossiveis:
        print("Quantidade informada é maior que a quantidade possível.")
    elif int(opcao) < subredesPossiveis:
        for i in range(int(opcao)):
            functions.exibirSubredes(i, primeiroEndereco)

# 3 - Transformar máscara CIDR
elif int(opcao) == 3:
    cidr = int(input("Insira o número CIDR: "))
    bitsExtras = cidr - 24
    binary = functions.decBitsToBinary(bitsExtras)
    mascara = functions.binaryToDecimal(binary)
    if cidr > 24:
        print("IP Classe C")
        print(f"Máscara 255.255.255.{mascara}")

# TODO: Configurar o colorama
# TODO: Colocar numero maximo possivel de subredes
# TODO: Configurar IPS classe A e B