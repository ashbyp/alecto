from gate_api import ApiClient, Configuration, SpotApi
from gate_api.models.ticker import Ticker


class GateIO:
    def __init__(self, conf: dict) -> None:
        self.config = Configuration(
            key=conf['private']['gate.io']['api_key'],
            secret=conf['private']['gate.io']['api_secret'],
            host=conf['public']['gate.io']['api_host']
        )
        self.spot_api = SpotApi(ApiClient(self.config))

    def get_all_tickers(self) -> list[Ticker]:
        tickers = self.spot_api.list_tickers()
        return tickers

    def get_ticker(self, ccy_pair: str) -> Ticker | None:
        tickers = self.spot_api.list_tickers(currency_pair=ccy_pair)
        if not tickers:
            print(f'Failed to find tickers for {ccy_pair}')
            return None
        return tickers[0]

    def get_last_price(self, ccy_pair: str) -> str | None:
        tickers = self.get_ticker(ccy_pair)
        if not tickers:
            print(f'Failed to find price for {ccy_pair}')
            return None
        return tickers.last


if __name__ == '__main__':
    from utils import config
    api = GateIO(config.get())
    ccys = ['BTC', 'ETH', 'VRA', 'DOT']

    for ccy in ccys:
        pair = f'{ccy}_USDT'
        price = api.get_last_price(pair)
        print(f'{pair} = {price}')

    print(api.get_ticker('BTC_USDT'))

