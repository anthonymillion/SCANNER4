import streamlit as st
import pandas as pd
from modules.option_flow import get_option_flow_signals
from modules.cot_fetcher import get_cot_signals
from modules.econ_event import get_economic_signals

st.set_page_config(layout="wide")
st.title("📊 Live Sentiment Scanner (EdgeFinder Style)")

cot = get_cot_signals()
econ = get_economic_signals()
flow = get_option_flow_signals()

signals = pd.concat([cot, econ, flow], axis=0, ignore_index=True)

if not signals.empty:
    st.dataframe(signals, use_container_width=True, height=600)
else:
    st.warning("No live signals available right now.")