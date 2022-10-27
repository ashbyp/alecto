import pprint
from market.gateioapi import GateIO
from market.coinmarketcapproapi import CoinmarketcapPRO
from market.binanceapi import Binance
from utils import config

conf = config.get()
gate = GateIO(conf)
coin = CoinmarketcapPRO(conf)
bin = Binance(conf)


def print_last_price(ccy_pair: str) -> None:
    g = gate.get_last_price(ccy_pair)
    c = coin.get_last_price(ccy_pair)
    b = bin.get_last_price(ccy_pair.replace('_', ''))
    print(f'{ccy_pair}: gate={g}, coin={c}, binance={b}')


def print_ticker(ccy_pair: str) -> None:
    print('GATE')
    print(gate.get_ticker(ccy_pair))
    print('COIN')
    print(coin.get_ticker(ccy_pair))
    print('BINANCE')
    print(bin.get_ticker(ccy_pair.replace('_', '')))


def main():
    print_last_price('BTC_USDT')
    print_last_price('ETH_USDT')
    print_last_price('DOGE_USDT')

    print_ticker('BTC_USDT')



if __name__ == '__main__':
    main()