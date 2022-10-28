from gate_api import ApiClient, Configuration, SpotApi, Order, WalletApi
from gate_api.models.ticker import Ticker


class GateIO:
    def __init__(self, conf: dict) -> None:
        self.config = Configuration(
            key=conf['private']['gate.io']['api_key'],
            secret=conf['private']['gate.io']['api_secret'],
            host=conf['public']['gate.io']['api_host']
        )
        client = ApiClient(self.config)
        self.spot_api = SpotApi(client)
        self.wallet_api = WalletApi(client)

    def get_spot_accounts(self):
        return self.spot_api.list_spot_accounts()

    def get_trades(self, ccy_pair:str):
        return self.spot_api.list_trades(ccy_pair)

    def get_ccy_list(self):
        return self.spot_api.list_currencies()

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

    def get_balance(self):
        return self.wallet_api.get_total_balance()

    def get_sub_account_balances(self):
        return self.wallet_api.list_sub_account_balances()


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

    print([ccy.currency for ccy in api.get_ccy_list()])

    print(api.get_balance())
    print(api.get_sub_account_balances())

    trades = api.get_trades('VRA_USDT')
    print(f'Num trades: {len(trades)}')
    print(f'Sum buy: {sum(float(x.amount) for x in trades if x.side=="buy")}')
    print(f'Sum sell: {sum(float(x.amount) for x in trades if x.side == "sell")}')

    for account in api.get_spot_accounts():
        print(account)


if __name__ == '__main__':
    main()