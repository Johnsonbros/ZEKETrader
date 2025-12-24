from typing import Literal, Union
from pydantic import BaseModel, Field, field_validator


class TradeIntent(BaseModel):
    action: Literal["TRADE"] = "TRADE"
    symbol: str
    side: Literal["buy", "sell"]
    notional_usd: float = Field(gt=0)
    confidence: float = Field(ge=0, le=1)
    reason: str
    
    @field_validator('symbol')
    @classmethod
    def uppercase_symbol(cls, v):
        return v.upper()


class NoTrade(BaseModel):
    action: Literal["NO_TRADE"] = "NO_TRADE"
    reason: str


Decision = Union[TradeIntent, NoTrade]
