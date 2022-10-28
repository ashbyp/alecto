from dataclasses import dataclass
from typing import Any


@dataclass
class Ticker:
    ccy_pair: str
    last_price: str
    raw: Any



