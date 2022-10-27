from binance import Client


class Binance:
    def __init__(self, conf: dict) -> None:
        self.client = Client(
            api_key=conf['private']['binance']['api_key'],
            api_secret=conf['private']['binance']['api_secret'])

    def get_all_tickers(self) -> list[dict[str, str]]:
        tickers = self.client.get_all_tickers()
        return tickers

    def get_ticker(self, ccy_pair) -> dict[str, str]:
        ticker = self.client.get_ticker(symbol=ccy_pair)
        return ticker

    def get_last_price(self, ccy_pair: str) -> str | None:
        ticker = self.get_ticker(ccy_pair)
        if not ticker:
            print(f'Failed to find price for {ccy_pair}')
            return None
        return ticker['lastPrice']


def main():
    from utils import config
    api = Binance(config.get())
    all_tickers = api.get_all_tickers()
    print(all_tickers[0])
    print([t['symbol'] for t in all_tickers if t['symbol'].startswith('BTC')])

    print(api.get_ticker("BTCUSDT"))


if __name__ == '__main__':
    main()
