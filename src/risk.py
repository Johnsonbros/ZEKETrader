from typing import Tuple
from src.schemas import Decision, TradeIntent, NoTrade
from src.config import Config


def risk_check(decision: Decision, cfg: Config) -> Tuple[bool, str]:
    """
    Perform risk checks on a trading decision.
    
    Args:
        decision: The trading decision to validate
        cfg: Configuration with risk limits
    
    Returns:
        Tuple of (allowed: bool, notes: str)
    """
    if isinstance(decision, NoTrade):
        return (True, "NO_TRADE decisions are always allowed")
    
    if isinstance(decision, TradeIntent):
        notes = []
        
        if decision.symbol not in cfg.allowed_symbols:
            return (False, f"Symbol {decision.symbol} not in allowlist: {cfg.allowed_symbols}")
        
        if decision.notional_usd > cfg.max_dollars_per_trade:
            return (
                False, 
                f"Trade size ${decision.notional_usd:.2f} exceeds max ${cfg.max_dollars_per_trade:.2f}"
            )
        
        notes.append(f"Symbol {decision.symbol} is allowed")
        notes.append(f"Trade size ${decision.notional_usd:.2f} within limits")
        
        return (True, "; ".join(notes))
    
    return (False, "Unknown decision type")
