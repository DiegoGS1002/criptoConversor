from cripto import *

def menu():
    print()
    print('1 - BITCOIN')
    print('2 - ETHEREUM')
    print('3 - SOLANA')
    print('4 - LINK')
    print('5 - DOGE')
    print('6 - Outra criptomoeda')
    print('0 - Sair')
opcao = 1

while opcao !=0:
    menu()
    opcao = int(input('Digite a opção desejada: '))
    match opcao:
        case 1: 
            origem = 'bitcoin' 
            destino = 'usd'
        case 2:
            origem = 'ethereum'
            destino = 'usd'
        case 3:
            origem = 'solana'
            destino = 'usd'
        case 4:
            origem = 'chainlink'
            destino = 'usd'
        case 5:
             origem = 'dogecoin'
             destino = 'usd'
        case 6:
            origem = input('Digite a criptomoeda: ')
            destino = input('Digite a moeda de destino: ')
        case 0:
            print('Saindo...')
    if opcao:
        print()
        print("******************************************************")
        rate = get_exchange_rate(origem, destino)
        if rate is not None:
            print(f"1 {origem} equivale a {rate} {destino}")
        else:
            print("Não foi possível obter a taxa de câmbio.")
        print("******************************************************")
        print()
