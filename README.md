# Zeke Trader - AI Trading Bot Skeleton

An AI-driven trading bot skeleton prepared for future integration with OpenAI Agents SDK and Alpaca via MCP. This is scaffolding only — no real trading or API calls are implemented.

## What This Project Is

This project provides the foundational structure for an AI trading system that will:
- Use OpenAI Agents SDK for decision making (coming soon)
- Execute trades via Alpaca MCP (coming soon)
- Visualize decisions through a Streamlit dashboard

Currently, the bot:
- Runs a continuous loop
- Logs stubbed decisions to CSV
- Displays logs on a dashboard
- All trading logic is placeholder/stubbed

## Running the Bot

```bash
python -m src.main
```

## Running the Dashboard

```bash
streamlit run dashboard/app.py --server.port 5000
```

## Setting Up Secrets in Replit

1. Open the "Secrets" tab in your Replit project
2. Add your API keys:
   - `OPENAI_API_KEY` - Your OpenAI API key
   - `ALPACA_KEY_ID` - Your Alpaca API key ID
   - `ALPACA_SECRET_KEY` - Your Alpaca secret key

**WARNING: Never commit API keys to version control. Never screenshot or share your API keys.**

## Trading Modes

The bot supports three trading modes configured via the `TRADING_MODE` environment variable:

### Paper Mode (`TRADING_MODE=paper`)
- Default mode
- Simulates trades without real money
- Safe for testing and development

### Shadow Mode (`TRADING_MODE=shadow`)
- Logs what trades *would* be made
- No actual orders are placed
- Useful for validating strategy before going live

### Live Mode (`TRADING_MODE=live`)
- Executes real trades with real money
- **Requires `LIVE_TRADING_ENABLED=true`** as an additional safety check
- Use with extreme caution

## Configuration

All configuration is done via environment variables. See `.env.example` for available options:

- `ALLOWED_SYMBOLS` - Comma-separated list of allowed trading symbols
- `MAX_DOLLARS_PER_TRADE` - Maximum dollars per single trade
- `MAX_OPEN_POSITIONS` - Maximum concurrent open positions
- `MAX_TRADES_PER_DAY` - Maximum trades allowed per day
- `MAX_DAILY_LOSS` - Maximum daily loss before stopping
- `LOOP_SECONDS` - Seconds between decision loops

## Project Structure

```
├── src/
│   ├── __init__.py
│   ├── main.py          # Main bot loop
│   ├── config.py        # Configuration loading
│   ├── schemas.py       # Pydantic data models
│   ├── agent_runner.py  # AI decision making (stub)
│   ├── risk.py          # Risk management
│   ├── broker_mcp.py    # Alpaca MCP broker (stub)
│   └── logger.py        # CSV logging
├── dashboard/
│   └── app.py           # Streamlit dashboard
├── logs/
│   └── decisions.csv    # Decision log (auto-created)
├── .env.example         # Environment variable template
└── README.md            # This file
```
