from gate_api import ApiClient, Configuration, SpotApi, Order
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
        ticker = self.spot_api.list_tickers(currency_pair=ccy_pair)
        if not ticker:
            print(f'Failed to find tickers for {ccy_pair}')
            return None
        return ticker[0]

    def get_last_price(self, ccy_pair: str) -> str | None:
        tickers = self.get_ticker(ccy_pair)
        if not tickers:
            print(f'Failed to find price for {ccy_pair}')
            return None
        return tickers.last

    def place_sell_order(self, ccy_pair: str, amount: float, price: float) -> Order:
        order = Order(amount=str(amount), price=str(price), side='sell', currency_pair=ccy_pair)
        created = self.spot_api.create_order(order)
        print(f'order created with id {created.id}, status {created.status}')
        return created

    def cancel_all_orders(self, ccy_pair: str) -> None:
        self.spot_api.cancel_orders(ccy_pair)


def main():
    from utils import config
    api = GateIO(config.get())
    ccys = ['BTC', 'ETH', 'VRA', 'DOT']

    for ccy in ccys:
        pair = f'{ccy}_USDT'
        price = api.get_last_price(pair)
        print(f'{pair} = {price}')

    print(api.get_ticker('BTC_USDT'))

    ccy_pair = 'VRA_USDT'
    order = api.place_sell_order(ccy_pair, 1000.0, float(api.get_last_price(ccy_pair)) * 10.0)
    print(order)

    api.cancel_all_orders(ccy_pair)


if __name__ == '__main__':
    main()