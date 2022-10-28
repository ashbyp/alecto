import logging
from enum import Enum, auto
from typing import Protocol, Optional
from market.types import Ticker
from utils import config


class Provider(Enum):
    GATE_IO = auto(),
    COIN_PRO = auto(),
    BINANCE = auto()


class DataProvider(Protocol):
    def get_supported_currencies(self) -> list[str]:
        ...

    def get_supported_currency_pairs(self) -> list[str]:
        ...

    def get_currency_info(self):
        ...

    def get_currency_pair_info(self, currency_pair: str):
        ...

    def get_last_price(self, ccy_pair: str) -> float:
        ...

    def get_last_prices(self, ccy_pairs: list[str]) -> dict[str, float]:
        ...

    def get_all_last_prices(self) -> dict[str, float]:
        ...

    def get_ticker(self, ccy_pair: str) -> Optional[Ticker]:
        ...

    def get_tickers(self, ccy_pair: list[str]) -> Optional[dict[str, Ticker]]:
        ...

    def get_all_tickers(self) -> Optional[dict[str, Ticker]]:
        ...


def get(provider: Provider) -> Optional[DataProvider]:
    match provider:
        case Provider.GATE_IO:
            from market.providers.gateioapi import GateIO
            return GateIO(config.get())
        case Provider.COIN_PRO:
            from market.providers.coinmarketcapproapi import CoinmarketcapPRO
            return CoinmarketcapPRO(config.get())
        case Provider.BINANCE:
            from market.providers.binanceapi import Binance
            return Binance(config.get)
        case _:
            logging.error(f"Invalid Provider specified: {provider}")
            return None


if __name__ == '__main__':
    print(Provider.COIN_PRO.value)