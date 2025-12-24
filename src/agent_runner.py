from src.schemas import Decision, NoTrade
from src.config import Config


def get_decision(market_snapshot: dict, cfg: Config) -> Decision:
    """
    Get a trading decision based on market data.
    
    TODO: Integrate OpenAI Agents SDK for real decision making
    TODO: Add MCP tools for market data and analysis
    TODO: Implement actual strategy logic
    
    Args:
        market_snapshot: Current market data including timestamp and prices
        cfg: Configuration object with trading parameters
    
    Returns:
        Decision: Either a TradeIntent or NoTrade decision
    """
    return NoTrade(
        action="NO_TRADE",
        reason="Skeleton running"
    )
