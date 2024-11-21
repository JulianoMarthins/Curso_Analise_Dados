import requests
import pandas as pd
from datetime import datetime
import time

requisicao = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL, BTC-BRL")

requisicao_dic = requisicao.json()
cotDolar = requisicao_dic["USD-BRL"]["bid"]
cotEuro = requisicao_dic["EUR-BRL"]["bid"]
cotBTC = requisicao_dic["BTC-BRL"]["bid"]

tabela = pd.read_excel("Cotações.xlsx")
tabela.loc[0, 'Cotação'] = float(cotDolar)
tabela.loc[1, 'Cotação'] = float(cotEuro)
tabela.loc[2, 'Cotação'] = float(cotBTC) * 1000
tabela.loc[0, "Data Última Atualização"] = datetime.now()

tabela.to_excel("Cotações.xlsx", index=False)

print(f"Cotação atualizada: {datetime.now()}")
