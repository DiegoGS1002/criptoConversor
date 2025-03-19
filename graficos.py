import matplotlib.pyplot as plt

# Função para gerar gráfico de barras
def graficoDeBarras():
    plt.bar()
    plt.title('Converções para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL')
    plt.show()

# Função para gerar gráfico de pizza
def graficoDePizza(l_moedas, l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção em relação ao Real (BRL)')
    plt.show()

# Função para gerar gráfico de dispersão
def graficoDeDispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Converções para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL')
    plt.show()

