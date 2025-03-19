import requests

def get_exchange_rate(origem ="bitcoin", destino="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={origem}&vs_currencies={destino}"
    response = requests.get(url)
    data = response.json()

    
    if response.status_code:
        if origem in data and destino in data[origem]:
            return data[origem][destino]
        else:
            print("Moeda não encontrada. Certifique-se de usar os nomes corretos.")
            return None
    else:
        print("Erro ao acessar a API.")
        return None
