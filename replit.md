# Zeke Trader - AI Trading Bot

## Overview

Zeke Trader is a skeleton/scaffolding project for an AI-driven trading bot. The project provides foundational structure for a future trading system that will integrate OpenAI Agents SDK for decision-making and Alpaca via MCP (Model Context Protocol) for trade execution. Currently, all trading logic is stubbed - the bot runs a continuous loop, logs placeholder decisions to CSV, and displays them on a Streamlit dashboard.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Application Structure

The project follows a modular Python architecture with clear separation of concerns:

- **Entry Point** (`src/main.py`): Contains the main bot loop that runs continuously, fetching decisions and logging them
- **Agent Runner** (`src/agent_runner.py`): Stub for OpenAI Agents SDK integration - currently returns NoTrade decisions
- **Broker Interface** (`src/broker_mcp.py`): Stub class for Alpaca MCP integration - methods raise NotImplementedError
- **Risk Management** (`src/risk.py`): Validates trading decisions against configurable limits (symbol allowlist, max trade size)
- **Configuration** (`src/config.py`): Pydantic-based config loading from environment variables with validation
- **Schemas** (`src/schemas.py`): Pydantic models for TradeIntent and NoTrade decisions
- **Logger** (`src/logger.py`): CSV-based logging of trading decisions

### Dashboard

A Streamlit dashboard (`dashboard/app.py`) provides real-time visualization of trading decisions by reading from the CSV log file. Runs on port 5000.

### Trading Modes

Three modes supported via `TRADING_MODE` environment variable:
- **Paper** (default): Simulates trades without real money
- **Shadow**: Logs what trades would be made without executing
- **Live**: Blocked by safety check requiring `LIVE_TRADING_ENABLED=true`

### Design Decisions

1. **Pydantic for validation**: All configuration and data schemas use Pydantic for type safety and validation
2. **CSV logging**: Simple, human-readable logging format that's easy to inspect and parse
3. **Safety-first approach**: Live trading requires explicit opt-in via two environment variables
4. **Stub architecture**: All external integrations (OpenAI, Alpaca) are stubbed with clear TODO markers for future implementation

## External Dependencies

### Python Packages
- **Pydantic**: Data validation and settings management
- **python-dotenv**: Environment variable loading from .env files
- **Streamlit**: Dashboard web interface
- **Pandas**: Data manipulation for dashboard display

### Future Integrations (Not Yet Implemented)
- **OpenAI Agents SDK**: Will handle AI-driven trading decisions
- **Alpaca via MCP**: Will handle trade execution and market data

### Required Secrets
Configure in Replit Secrets tab:
- `OPENAI_API_KEY`: OpenAI API key (for future use)
- `ALPACA_KEY_ID`: Alpaca API key ID (for future use)
- `ALPACA_SECRET_KEY`: Alpaca secret key (for future use)

### Data Storage
- **CSV Files** (`logs/decisions.csv`): Stores all trading decisions with timestamps, actions, confidence levels, and risk check results