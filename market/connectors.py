from market.binanceapi import Binance
from market.coinmarketcapproapi import CoinmarketcapPRO
from market.gateioapi import GateIO
from utils import config

conf = config.get()
gate_api = GateIO(conf)
coin_api = CoinmarketcapPRO(conf)
bin_api = Binance(conf)


def print_last_price(ccy_pair: str) -> None:
    g = gate_api.get_last_price(ccy_pair)
    c = coin_api.get_last_price(ccy_pair)
    b = bin_api.get_last_price(ccy_pair.replace('_', ''))

    print(type(g), type(c), type(b))

    print(f'{ccy_pair}: gate_api={g}, coin_api={c}, binance={b}')


def print_ticker(ccy_pair: str) -> None:
    print('GATE')
    print(gate_api.get_ticker(ccy_pair))
    print('COIN')
    print(coin_api.get_ticker(ccy_pair))
    print('BINANCE')
    print(bin_api.get_ticker(ccy_pair.replace('_', '')))


def main():
    print_last_price('BTC_USDT')
    print_last_price('ETH_USDT')
    print_last_price('DOGE_USDT')

    print_ticker('BTC_USDT')



if __name__ == '__main__':
    main()