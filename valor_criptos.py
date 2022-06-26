import json
import requests
import pandas as pd
import time

status = "a"
try:
    while status !="q":
        master = []
        coin_list_btc = []
        coin_list_eth = []
        coin_list_ada = []
# obteniendo el precio actual de BITCOIN
        btc = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true').text
        btc = json.loads(btc)
#print(btc['bitcoin'])
        btc = btc['bitcoin']
        for key, value in btc.items():
            coin_list_btc.append(value)
        #print(coin_list_btc)
        master.append(coin_list_btc)

# obteniendo el precio actual de ETHEREUM
        eth = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=true').text
        eth = json.loads(eth)
#print(eth)
        eth = eth['ethereum']
        for key, value in eth.items():
            coin_list_eth.append(value)
        #print(coin_list_eth)
        master.append(coin_list_eth)

# obteniendo el precio actual de CARDANO
        ada = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_market_cap=true').text
        ada = json.loads(ada)
#print(ada)
        ada = ada['cardano']
        for key, value in ada.items():
            coin_list_ada.append(value)
        #print(coin_list_ada)
        master.append(coin_list_ada)

        time.sleep(1)
        df = pd.DataFrame(master, columns = ["Price", "Market Cap"], index=["BTC","ETH","ADA"])
        print("\n",df)
        status = input("\nPresione cualquier tecla para actualizar los precios o 'q'para salir: ")
except:
    print("Ha surgido un error")