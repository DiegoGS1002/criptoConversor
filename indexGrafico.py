from graficos import *
from moedas import get_cotacao
cotacoes = get_cotacao()

# Listas de moedas e valores
l_moedas = ['USD - DOLAR', 'EUR - EURO', 'GBP - LIBRA'] 
# Inverter a cotação para obter o valor da moeda em relação ao Real
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]   

# Função para exibir o menu
def menu():
    print('==================================')
    print('1 - Gráfico de Barras')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Sair')
    print('==================================')

opcao = 1

while opcao != 0:

    menu()
    opcao = int(input('Escolha um tipo de gráfico:'))

    match opcao:
        case 1: graficoDeBarras()
        case 2: graficoDePizza(l_moedas, l_valores)
        case 3: graficoDeDispersao(l_moedas, l_valores)
        case 0: print('Saindo...')
