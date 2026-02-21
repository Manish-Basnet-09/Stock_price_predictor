
from pydantic import BaseModel

class StockInput(BaseModel):
    open: float
    high: float
    low: float
    close: float
    traded_quantity: float
    ma_5: float
    ma_10: float
    vol_ma_5: float
    close_lag1: float
    momentum_3: float
    volatility_5: float
    price_change: float