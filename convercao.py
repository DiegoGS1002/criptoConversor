from moedas import converterCotacao

def menu():
    print()
    print('1 - Converter BTC em BRL')
    print('2 - Converter ETH em BRL')
    print('3 - Converter SOL em BRL')
    print('4 - Outra conversão')
    print('0 - Sair')

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Digite a opção desejada: '))
    destino = 'BRL'
    valor = int(input('Digite o valor a ser convertido: '))
    match opcao:
        case 1:
            origem = 'BTC'
        case 2:
            origem = 'EUR'
        case 3:
            origem = 'GBP'
        case 4:
            origem = input('Digite a moeda de origem: ')
            destino = input('Digite a moeda de destino: ')
        case 0:
            print('Saindo...')
    
    if opcao:
        print()
        print("**********************************")
        print(f"{origem} para {destino}", converterCotacao(origem, destino, valor))
        print("**********************************")
        print()
