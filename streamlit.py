import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
from PIL import Image
from configs import *

# --- 1. CONFIGURATION (Custom Layout and Appearance) ---
im = Image.open("favicon.png")

st.set_page_config(
    page_title="Rheo Investment Dashboard",
    page_icon=im,
    initial_sidebar_state="expanded",
    layout="centered" # or "wide" for a full-screen layout
)

# --- 2. AUTHENTICATION FUNCTIONS AND STATE MANAGEMENT ---

# Initialize the session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'

def authenticate_user(username, password):
    """Checks credentials against hardcoded values for demonstration."""

    # Read demo username and pw from configs
    if username == DEMO_USER and password == DEMO_PASS:
        st.session_state['authenticated'] = True
        # Using success here is fine, but st.rerun() will clear it quickly
        st.rerun() # Rerun to trigger the dashboard view
    else:
        st.error("Invalid username or password.")

def logout():
    """Resets the authentication status."""
    st.session_state['authenticated'] = False
    st.rerun() # Rerun to show the login page

# --- 3. MAIN APPLICATION LOGIC ---

if not st.session_state.authenticated:
    # --- LOGIN PAGE ---
    st.title("Rheo Investment Demo")
    
    # Center the login form for a cleaner look
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.subheader("Please Log In")
        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username", value="demo")
            password = st.text_input("Password", type="password", value="12345")
            
            # Use a primary color button for emphasis
            submitted = st.form_submit_button("Login", type="primary")

            if submitted:
                authenticate_user(username, password)
                
else:
    # Sidebar Navigation
    with st.sidebar:
        st.title("Navigation")
        st.divider()
        
        # Navigation buttons
        if st.button("📊 Dashboard", width="stretch", key="nav_dashboard"):
            st.session_state.page = 'dashboard'
        
        if st.button("💼 Portfolio", width="stretch", key="nav_portfolio"):
            st.session_state.page = 'portfolio'
        
        if st.button("📈 Market Insights", width="stretch", key="nav_market"):
            st.session_state.page = 'market_insights'
        
        if st.button("💰 Investment", width="stretch", key="nav_investment"):
            st.session_state.page = 'investment'
        
        if st.button("📋 Token List", width="stretch", key="nav_tokens"):
            st.session_state.page = 'token_list'
        
        if st.button("👛 Wallet", width="stretch", key="nav_wallet"):
            st.session_state.page = 'wallet'
        
        if st.button("⚙️ Settings", width="stretch", key="nav_settings"):
            st.session_state.page = 'settings'
        
        st.divider()
        
        if st.button("🚪 Logout", width="stretch", key="nav_logout"):
            logout()
        
        st.divider()
        st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # --- DASHBOARD PAGE ---
    # Page content based on selection
    if st.session_state.page == 'dashboard':
        st.title("📊 Dashboard")
        
        # Top 2 columns
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Portfolio Value", "$45,231.89", "+2.5%")
            st.info("Your portfolio is performing well!")
        with col2:
            st.metric("24h Change", "+$1,123.45", "+2.5%")
            st.success("All assets are up today")
        
        st.divider()
        
        # Bottom 3 columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Bitcoin", "$35,000", "+5.2%")
        with col2:
            st.metric("Ethereum", "$2,100", "+3.1%")
        with col3:
            st.metric("Total Return", "+45.2%", "+2.1%")


    elif st.session_state.page == 'portfolio':
        st.title("💼 Portfolio")
        
        # Row 1
        st.subheader("Holdings Overview")
        col1, col2 = st.columns(2)
        with col1:
            st.write("📊 Your current holdings:")
            portfolio_data = {
                'Asset': ['Bitcoin', 'Ethereum', 'Cardano'],
                'Amount': [0.5, 5.2, 100],
                'Value': ['$17,500', '$10,920', '$45']
            }
            st.dataframe(pd.DataFrame(portfolio_data), width="stretch")
        with col2:
            st.write("📈 Performance:")
            performance_data = {
                'Asset': ['Bitcoin', 'Ethereum', 'Cardano'],
                '24h': ['+5.2%', '+3.1%', '-2.1%'],
                '7d': ['+12.5%', '+8.3%', '+1.2%']
            }
            st.dataframe(pd.DataFrame(performance_data), width="stretch")
        
        st.divider()
        
        # Row 2
        st.subheader("Allocation")
        allocation_data = {
            'Asset': ['Bitcoin', 'Ethereum', 'Cardano', 'Cash'],
            'Percentage': [38.7, 24.2, 0.1, 37.0]
        }
        st.bar_chart(pd.DataFrame(allocation_data).set_index('Asset'))


    elif st.session_state.page == 'market_insights':
        st.title("📈 Market Insights")
        
        # Top 3 columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Market Cap", "$2.4T", "+3.2%")
        with col2:
            st.metric("Bitcoin Dominance", "48.3%", "+1.2%")
        with col3:
            st.metric("Total Volume", "$85.2B", "+12.5%")
        
        st.divider()
        
        # Bottom 1 column
        st.subheader("Market Trends")
        st.line_chart({
            'Bitcoin': [30000, 31000, 32000, 33000, 34000, 35000],
            'Ethereum': [1800, 1850, 1900, 1950, 2000, 2100],
            'Market': [2200, 2250, 2300, 2350, 2400, 2450]
        })


    elif st.session_state.page == 'investment':
        st.title("💰 Investment Opportunities")
        
        # 3x2 grid of investments
        investments = [
            {"title": "Bitcoin Fund", "image": "🪙"},
            {"title": "Ethereum Fund", "image": "🔷"},
            {"title": "DeFi Portfolio", "image": "🏦"},
            {"title": "NFT Collection", "image": "🖼️"},
            {"title": "Staking Pool", "image": "🎁"},
            {"title": "Yield Farming", "image": "🌾"}
        ]
        
        cols = st.columns(3)
        for idx, investment in enumerate(investments):
            with cols[idx % 3]:
                with st.container(border=True):
                    st.write(investment["image"])
                    st.subheader(investment["title"])
                    if st.button(f"Explore", key=f"invest_{idx}"):
                        st.switch_page(f"pages/investment_detail_{idx}.py")


    elif st.session_state.page == 'token_list':
        st.title("📋 Token List")
        
        # Create sample CSV data if it doesn't exist
        csv_file = "tokens.csv"
        if not os.path.exists(csv_file):
            sample_data = {
                'Symbol': ['BTC', 'ETH', 'ADA', 'SOL', 'XRP'],
                'Name': ['Bitcoin', 'Ethereum', 'Cardano', 'Solana', 'Ripple'],
                'Price': ['$35,000', '$2,100', '$0.45', '$98', '$2.50'],
                '24h Change': ['+5.2%', '+3.1%', '-2.1%', '+8.5%', '-1.3%'],
                'Market Cap': ['$680B', '$252B', '$16B', '$42B', '$135B']
            }
            df = pd.DataFrame(sample_data)
            df.to_csv(csv_file, index=False)
        else:
            df = pd.read_csv(csv_file)
        
        # Display table
        st.dataframe(df, width="stretch")
        
        # Option to upload new CSV
        uploaded_file = st.file_uploader("Upload tokens CSV", type="csv")
        if uploaded_file is not None:
            df_new = pd.read_csv(uploaded_file)
            st.dataframe(df_new, width="stretch")


    elif st.session_state.page == 'wallet':
        st.title("👛 Wallet")
        
        # Row 1 - 2 columns
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Balance", "$45,231.89")
            st.info("Wallet Address: 0x742d...8D5c")
        with col2:
            st.metric("Pending Transactions", "2")
            st.warning("2 transactions awaiting confirmation")
        
        st.divider()
        
        # Row 2 - 1 column
        st.subheader("Recent Transactions")
        transactions = {
            'Date': ['2024-01-15', '2024-01-14', '2024-01-13'],
            'Type': ['Receive', 'Send', 'Swap'],
            'Amount': ['+2.5 BTC', '-0.5 ETH', '10 ADA → 5 SOL'],
            'Status': ['Confirmed', 'Confirmed', 'Pending']
        }
        st.dataframe(pd.DataFrame(transactions), width="stretch")


    elif st.session_state.page == 'settings':
        st.title("⚙️ Settings")
        
        st.subheader("Preferences")
        
        # Buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔑 Change Password"):
                st.success("Password change initiated")
        with col2:
            if st.button("🔔 Notification Preferences"):
                st.info("Redirecting to notifications...")
        with col3:
            if st.button("💾 Export Data"):
                st.success("Data export started")
        
        st.divider()
        
        # Dropdowns
        st.subheader("Configuration")
        
        col1, col2 = st.columns(2)
        with col1:
            theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
            st.caption(f"Selected theme: {theme}")
        with col2:
            currency = st.selectbox("Display Currency", ["USD", "EUR", "GBP", "JPY"])
            st.caption(f"Selected currency: {currency}")
        
        col1, col2 = st.columns(2)
        with col1:
            language = st.selectbox("Language", ["English", "Spanish", "French", "German"])
            st.caption(f"Selected language: {language}")
        with col2:
            update_freq = st.selectbox("Update Frequency", ["Real-time", "5 minutes", "15 minutes", "Hourly"])
            st.caption(f"Selected frequency: {update_freq}")
        
        st.divider()
        
        if st.button("💾 Save Settings"):
            st.success("Settings saved successfully!")


    elif st.session_state.page == 'logout':
        st.title("🚪 Logout")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.warning("Are you sure you want to logout?")
            
            if st.button("✅ Yes, Logout", width="stretch"):
                st.session_state.logged_in = False
                st.success("You have been logged out successfully!")
                st.info("Redirecting to login page...")
                # In a real app, you would redirect to login
                st.session_state.page = 'dashboard'
            
            if st.button("❌ Cancel", width="stretch"):
                st.session_state.page = 'dashboard'
                st.rerun()  