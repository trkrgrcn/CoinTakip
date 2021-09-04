import sqlite3
import json
conn = sqlite3.connect('cmcCoins.db')
cursor = conn.cursor()
from coinmarketcapapi import CoinMarketCapAPI

with open('apikey.json') as file:
    data = json.load(file)

cmc = CoinMarketCapAPI(data['cmcApi'])

def updateCoinTable():
    data_id_map = cmc.cryptocurrency_map()

    for i in range(0, 10000):
        cmcid = str(data_id_map.data[i]['id'])
        name = str(data_id_map.data[i]['name'])
        symbol = str(data_id_map.data[i]['symbol'])
        slug = str(data_id_map.data[i]['slug'])
        rank = str(data_id_map.data[i]['rank'])
        if str(data_id_map.data[i]['platform']) == 'None':
            token_address = '0'
            block_chain_name = 'None'
        else:
            token_address = str(data_id_map.data[i]['platform']['token_address'])
            block_chain_name = str(data_id_map.data[i]['platform']['name']) + ' (' + str(
                data_id_map.data[i]['platform']['symbol']) + ')'

        price = cmc.tools_priceconversion(amount=1, symbol=symbol, convert='USD')
        prc = str(price.data['quote']['USD']['price'])

        cursor.execute("INSERT INTO cmc_coin_list Values(?,?,?,?,?,?,?,?)",
                       (cmcid, name, symbol, slug, rank, token_address, block_chain_name, prc))
        conn.commit()

    conn.close()
