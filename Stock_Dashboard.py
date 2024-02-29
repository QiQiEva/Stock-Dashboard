import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import datetime
from alpha_vantage.fundamentaldata import FundamentalData
import os
from dotenv import load_dotenv


today = datetime.date.today()

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Enter Ticker', 'MSFT')
start_date = st.sidebar.date_input('Start Date', pd.to_datetime(today - datetime.timedelta(weeks=52))) # Set start date to 52 weeks ago
end_date = st.sidebar.date_input('End Date', pd.to_datetime(today)) # set end date to today

# Download data from yahoo finance
data = yf.download(ticker, start=start_date, end=end_date)

fig = px.line(data, x=data.index, y=data['Adj Close'], title=f'{ticker} Stock Price')   

st.plotly_chart(fig)

pricing_data, fundamental_data = st.tabs(["Pricing Data", "Fundamental Data"])

with pricing_data:
    st.header('Pricing Data')
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace=True)
    st.write(data2)
    # Annual Return
    annual_return = data2['% Change'].mean() * 252 * 100
    st.write(f'Annual Return: ', annual_return, '%')
    # Standard Deviation
    stdev = np.std(data2['% Change'])* np.sqrt(252) * 100
    st.write('Standard Deviation: ', stdev*100, '%')
    st.write('Risk Adj. Return is ', annual_return / (stdev*100))

# Load API Key from .env file 
# API Website: https://www.alphavantage.co/support/#api-key
load_dotenv()
api_key = os.getenv('API_KEY')

with fundamental_data:
    key = api_key
    fd = FundamentalData(key, output_format='pandas')

    # Balance Sheet
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    
    # Income Statement
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    
    # Cash Flow
    st.subheader('Cash Flow')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)