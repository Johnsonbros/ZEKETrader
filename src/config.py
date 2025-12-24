import os
from typing import List
from pydantic import BaseModel, field_validator
from dotenv import load_dotenv

load_dotenv()


class Config(BaseModel):
    openai_api_key: str = ""
    alpaca_key_id: str = ""
    alpaca_secret_key: str = ""
    
    trading_mode: str = "paper"
    live_trading_enabled: bool = False
    
    allowed_symbols: List[str] = []
    
    max_dollars_per_trade: float = 25.0
    max_open_positions: int = 3
    max_trades_per_day: int = 5
    max_daily_loss: float = 25.0
    
    loop_seconds: int = 60
    log_dir: str = "logs"
    
    @field_validator('trading_mode')
    @classmethod
    def validate_trading_mode(cls, v):
        valid_modes = ['paper', 'shadow', 'live']
        if v.lower() not in valid_modes:
            raise ValueError(f"TRADING_MODE must be one of: {valid_modes}")
        return v.lower()
    
    def model_post_init(self, __context):
        if self.trading_mode == "live" and not self.live_trading_enabled:
            raise ValueError(
                "LIVE TRADING BLOCKED: TRADING_MODE is set to 'live' but "
                "LIVE_TRADING_ENABLED is not 'true'. This is a safety check. "
                "Set LIVE_TRADING_ENABLED=true to enable live trading."
            )


def load_config() -> Config:
    symbols_str = os.getenv("ALLOWED_SYMBOLS", "NVDA,SPY,META,GOOGL,AVGO,BRK.A,GOOG,BRK.B,AMZN")
    allowed_symbols = [s.strip().upper() for s in symbols_str.split(",") if s.strip()]
    
    live_enabled_str = os.getenv("LIVE_TRADING_ENABLED", "false").lower()
    live_trading_enabled = live_enabled_str == "true"
    
    return Config(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        alpaca_key_id=os.getenv("ALPACA_KEY_ID", ""),
        alpaca_secret_key=os.getenv("ALPACA_SECRET_KEY", ""),
        trading_mode=os.getenv("TRADING_MODE", "paper"),
        live_trading_enabled=live_trading_enabled,
        allowed_symbols=allowed_symbols,
        max_dollars_per_trade=float(os.getenv("MAX_DOLLARS_PER_TRADE", "25")),
        max_open_positions=int(os.getenv("MAX_OPEN_POSITIONS", "3")),
        max_trades_per_day=int(os.getenv("MAX_TRADES_PER_DAY", "5")),
        max_daily_loss=float(os.getenv("MAX_DAILY_LOSS", "25")),
        loop_seconds=int(os.getenv("LOOP_SECONDS", "60")),
        log_dir=os.getenv("LOG_DIR", "logs"),
    )
