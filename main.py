import coin
import update

def main():
    tableUpdate = input('Tabloyu güncellemek ister misiniz? Y/N')
    if tableUpdate.upper()=='Y':
        update.updateCoinTable()
    else:
        cmc = coin.Coin()
        coinSymbol = input('Coin Sembol: ')
        coinInfo = cmc.__selectCoin__(column='*', table='cmc_coin_list', conditionWord='where',
                                      conditionColumn='symbol=', conditionValue=coinSymbol.upper())

        print(coinInfo)





if __name__ == '__main__':
    main()