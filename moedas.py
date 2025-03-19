import requests

# Função para obter a cotação
def get_cotacao(from_currency="bitcoin", to_currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={from_currency}&vs_currencies={to_currency}"
    response = requests.get(url)
    data = response.json() 

    if response.status_code == 200:
        return data['rates']
    else:
        print("Erro ao obter cotação", response.status_code)
        return None
    
# Função para converter a cotação
def converterCotacao(from_currency = 'BTC', to_currency = 'BRL', valor=1):
    rates = get_cotacao(to_currency)
    return round(valor / rates[from_currency],3)
