import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import datetime

today = datetime.date.today()

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Enter Ticker')
start_date = st.sidebar.date_input('Start Date', pd.to_datetime(today - datetime.timedelta(weeks=1))) # Set start date to 1 week ago
end_date = st.sidebar.date_input('End Date', pd.to_datetime(today)) # set end date to today

# Download data from yahoo finance
data = yf.download(ticker, start=start_date, end=end_date)

fig = px.line(data, x=data.index, y=data['Adj Close'], title=f'{ticker} Stock Price')
st.plotly_chart(fig)