import pprint
from market.gateio import GateIO
from market.coinmarketcappro import CoinmarketcapPRO
from utils import config


def main():
    conf = config.get()
    gate = GateIO(conf)
    coin = CoinmarketcapPRO(conf)

    ccy_pair = 'BTC_USD'
    print(f'{ccy_pair}: gate={gate.get_last_price(ccy_pair)}, coin={coin.get_last_price(ccy_pair)}')
    ccy_pair = 'ETH_USD'
    print(f'{ccy_pair}: gate={gate.get_last_price(ccy_pair)}, coin={coin.get_last_price(ccy_pair)}')
    ccy_pair = 'BTC_USDT'
    print(f'{ccy_pair}: gate={gate.get_last_price(ccy_pair)}, coin={coin.get_last_price(ccy_pair)}')

    ccy_pair = 'BTC_USD'
    g = gate.get_ticker(ccy_pair)
    c = coin.get_ticker(ccy_pair)
    print(f'GATE -{type(g)}----------------------------')
    pprint.pprint(g)
    print(f'COIN -{type(c)}----------------------------')
    pprint.pprint(c)


if __name__ == '__main__':
    main()