import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import webbrowser

# --- CONFIG ---
st.set_page_config(page_title="SSM Pro - Investment", page_icon="📈", layout="wide")

# --- CUSTOM CSS (LA SAXAY) ---
st.markdown("<style>.main { background-color: #111111; color: white; } .stButton>button { background-color: #00FF7F; color: black; border-radius: 5px; width: 100%; font-weight: bold; } .balance-card { background-color: #102A12; border: 1px solid #00FF7F; padding: 25px; border-radius: 15px; text-align: center; }</style>", unsafe_allow_name=True)

# --- SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- API BTC ---
def get_btc_price():
    try:
        res = requests.get("https://coingecko.com").json()
        return res['bitcoin']['usd']
    except:
        return 67000.0

# --- SIDEBAR ---
with st.sidebar:
    st.title("SSM PRO")
    lang = st.radio("Luuqadda / Language", ["Somali", "English"])
    
    if st.session_state.logged_in:
        st.markdown("---")
        st.write(f"👤 **{st.session_state.user}**")
        st.write("✅ *Verified Investor*")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

# --- LOGIN PAGE ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("Welcome to SSM")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("LOGIN / SIGNUP"):
            if u and p:
                st.session_state.logged_in = True
                st.session_state.user = u
                st.rerun()
# --- DASHBOARD PAGE ---
else:
    btc_p = get_btc_price()
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.markdown(f"""<div class='balance-card'>
            <p style='color:#00FF7F;'>TOTAL WEALTH</p>
            <h1 style='font-size:45px;'>$2,450.75</h1>
            <p style='color:grey;'>+5.4% Last 24h</p>
        </div>""", unsafe_allow_name=True)
        
        # Chart
        st.write("")
        fig = go.Figure(go.Scatter(y=[65000, 66500, 65800, 67400, btc_p], mode='lines+markers', line=dict(color='#00FF7F', width=3)))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=350)
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        st.subheader("Live Market")
        st.metric("Bitcoin (BTC)", f"${btc_p:,.2f}", "+1.2%")
        
        st.markdown("---")
        st.subheader("💰 Deposit")
        with st.expander("EVC Plus Helper"):
            st.write("1. Dial *712#")
            st.write("2. Send to: **061XXXXXXX**")
            st.write("3. Copy TXID to Chat")
        
        if st.button("💬 WhatsApp Support"):
            st.write("Guji link-ga: https://wa.me")

    # Portfolio
    st.markdown("---")
    st.subheader("Portfolio Status")
    df = pd.DataFrame({
        "Asset": ["Bitcoin", "Cash (USD)"],
        "Amount": ["0.015 BTC", "$1,450.75"],
        "Value": [f"${0.015*btc_p:,.2f}", "$1,450.75"]
    })
    st.table(df)
