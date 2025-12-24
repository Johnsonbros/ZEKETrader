import streamlit as st
import pandas as pd
from pathlib import Path
import time

st.set_page_config(
    page_title="Zeke Trader Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Zeke Trader Dashboard")
st.markdown("Real-time view of trading bot decisions")

LOG_PATH = Path("logs/decisions.csv")

def load_decisions():
    """Load decisions from CSV file."""
    if not LOG_PATH.exists():
        return None
    try:
        df = pd.read_csv(LOG_PATH)
        return df
    except Exception as e:
        st.error(f"Error loading log file: {e}")
        return None

placeholder = st.empty()

while True:
    with placeholder.container():
        df = load_decisions()
        
        if df is None or df.empty:
            st.info("No decisions logged yet. Start the bot with: `python -m src.main`")
        else:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Decisions", len(df))
            
            with col2:
                trades = len(df[df['action'] == 'TRADE']) if 'action' in df.columns else 0
                st.metric("Trade Decisions", trades)
            
            with col3:
                no_trades = len(df[df['action'] == 'NO_TRADE']) if 'action' in df.columns else 0
                st.metric("No Trade Decisions", no_trades)
            
            with col4:
                if 'mode' in df.columns and len(df) > 0:
                    mode = df['mode'].iloc[-1].upper()
                else:
                    mode = "UNKNOWN"
                st.metric("Current Mode", mode)
            
            st.markdown("---")
            st.subheader("Recent Decisions (Last 50)")
            
            recent = df.tail(50).iloc[::-1]
            
            st.dataframe(
                recent,
                use_container_width=True,
                hide_index=True
            )
    
    time.sleep(2)
    st.rerun()
