from requests import Session
import json


class CoinmarketcapPRO:

    def __init__(self, conf: dict) -> None:
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': conf['private']['coinmarketcap.pro']['api_key'],
        }
        self.session = Session()
        self.session.headers.update(headers)
        self.base_url = conf['public']['coinmarketcap.pro']['api_host']

    def get_ticker(self, ccy_pair: str) -> dict:
        ccy1, ccy2 = ccy_pair.split('_')

        parameters = {
            'symbol': ccy1,
            'convert': ccy2,
        }

        data = self._request("cryptocurrency/quotes/latest", parameters)
        return data

    def get_last_price(self, ccy_pair: str) -> str | None:
        ticker = self.get_ticker(ccy_pair)
        if not ticker:
            print(f'Failed to find price for {ccy_pair}')
            return None
        ccy1, ccy2 = ccy_pair.split('_')
        return ticker[ccy1]['quote'][ccy2]['price']

    def _request(self, request_name: str, parameters: dict) -> dict | None:
        url = f'{self.base_url}/{request_name}'
        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text).get('data')
            if not data:
                print(f'No data in response\n{url}\n{parameters}\n{response}')
                return None
            return data
        except Exception as e:
            print(f'Failed to make request\n{url}\n{parameters}\n{e}')
            return None


def main():
    from utils import config
    api = CoinmarketcapPRO(config.get())

    # print(api.get_ticker('BTC_USD'))
    # print(api.get_ticker('BTC_EUR'))
    print(api.get_last_price('BTC_USD'))
    print(api.get_last_price('BTC_EUR'))
    print(api.get_last_price('BTC_ETH'))


if __name__ == '__main__':
    main()
