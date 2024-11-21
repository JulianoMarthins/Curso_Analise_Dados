import requests
import pandas as pd
from datetime import datetime
import time

for i in range(2):
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    try:
        cotDolar = requisicao_dic["USDBRL"]["bid"]
        cotEuro = requisicao_dic["EURBRL"]["bid"]
        cotBTC = requisicao_dic["BTCBRL"]["bid"]
    except:
        print("Erro ao acessar a API")

    tabela = pd.read_excel("Cotações.xlsx")
    tabela.loc[0, 'Cotação'] = float(cotDolar)
    tabela.loc[1, 'Cotação'] = float(cotEuro)
    tabela.loc[2, 'Cotação'] = float(cotBTC) * 1000
    tabela.loc[0, "Data Última Atualização"] = datetime.now()

    try:
        tabela.to_excel("Cotações.xlsx", index=False)
    except:
        print("Erro ao salvar arquivo")
    print(f"Cotação atualizada: {datetime.now()}")

    time.sleep(60)
