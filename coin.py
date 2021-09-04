
import sqlite3

class Coin():

    def __init__(self):
        self.conn = sqlite3.connect('cmcCoins.db')
        self.cursor = self.conn.cursor()

    def __selectCoin__(self, **kwargs):
        table = kwargs.get('table','')
        conditionColumn = kwargs.get('conditionColumn', '')
        conditionValue = kwargs.get('conditionValue', '')
        column = kwargs.get('column', '*')
        conditionWord = kwargs.get('conditionWord', '')
        sql = "select {0} from {1} {2} {3} '{4}'".format(column, table, conditionWord, conditionColumn, conditionValue)
        # sql = 'select * from cmc_coin_list where symbol='"ETH"''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def __addCoin__(self, **kwargs):
        pass

    def __delCoin__(self):
        pass

