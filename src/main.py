import time
from datetime import datetime

from src.config import load_config
from src.agent_runner import get_decision
from src.risk import risk_check
from src.logger import log_decision
from src.schemas import TradeIntent


def print_banner(cfg):
    """Print startup banner."""
    print("=" * 60)
    print("  ZEKE TRADER - AI Trading Bot")
    print("=" * 60)
    print(f"  Mode: {cfg.trading_mode.upper()}")
    print(f"  Allowed Symbols: {', '.join(cfg.allowed_symbols)}")
    print(f"  Max $ per Trade: ${cfg.max_dollars_per_trade}")
    print(f"  Loop Interval: {cfg.loop_seconds}s")
    print("=" * 60)
    print()


def main():
    """Main bot loop."""
    cfg = load_config()
    print_banner(cfg)
    
    print("[INFO] Starting trading loop...")
    print("[INFO] Press Ctrl+C to stop")
    print()
    
    loop_count = 0
    
    while True:
        loop_count += 1
        ts = datetime.now()
        
        market_snapshot = {
            "timestamp": ts.isoformat(),
            "allowed_symbols": cfg.allowed_symbols,
            "loop_count": loop_count
        }
        
        decision = get_decision(market_snapshot, cfg)
        
        allowed, risk_notes = risk_check(decision, cfg)
        
        if isinstance(decision, TradeIntent):
            symbol = decision.symbol
            action = decision.action
            confidence = decision.confidence
            reason = decision.reason
        else:
            symbol = ""
            action = decision.action
            confidence = 0.0
            reason = decision.reason
        
        log_decision(
            ts=ts,
            mode=cfg.trading_mode,
            symbol=symbol,
            action=action,
            confidence=confidence,
            reason=reason,
            risk_allowed=allowed,
            risk_notes=risk_notes,
            log_dir=cfg.log_dir
        )
        
        print(f"[{ts.strftime('%H:%M:%S')}] Loop {loop_count}: {action} | {reason}")
        
        time.sleep(cfg.loop_seconds)


if __name__ == "__main__":
    main()
