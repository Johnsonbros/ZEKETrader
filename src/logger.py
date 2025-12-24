import os
import csv
from datetime import datetime
from pathlib import Path


LOG_HEADERS = [
    "timestamp",
    "mode",
    "symbol",
    "action",
    "confidence",
    "reason",
    "risk_allowed",
    "risk_notes"
]


def ensure_log_dir(log_dir: str = "logs") -> Path:
    """Ensure the logs directory exists."""
    path = Path(log_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_log_path(log_dir: str = "logs") -> Path:
    """Get the path to the decisions CSV file."""
    return ensure_log_dir(log_dir) / "decisions.csv"


def ensure_csv_header(log_path: Path) -> None:
    """Create the CSV file with headers if it doesn't exist."""
    if not log_path.exists():
        with open(log_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(LOG_HEADERS)


def log_decision(
    ts: datetime,
    mode: str,
    symbol: str,
    action: str,
    confidence: float,
    reason: str,
    risk_allowed: bool,
    risk_notes: str,
    log_dir: str = "logs"
) -> None:
    """
    Append a decision to the CSV log file.
    
    Args:
        ts: Timestamp of the decision
        mode: Trading mode (paper, shadow, live)
        symbol: Stock symbol or empty for NO_TRADE
        action: TRADE or NO_TRADE
        confidence: Confidence score 0-1
        reason: Reason for the decision
        risk_allowed: Whether risk check passed
        risk_notes: Notes from risk check
        log_dir: Directory for log files
    """
    log_path = get_log_path(log_dir)
    ensure_csv_header(log_path)
    
    with open(log_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            ts.isoformat(),
            mode,
            symbol,
            action,
            f"{confidence:.4f}" if confidence else "",
            reason,
            str(risk_allowed),
            risk_notes
        ])
