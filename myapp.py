import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Simple Stock Price App
""")
st.write("""
## Google
""")
#define ticker volume
tickerSymbol='GOOGL'
#define ticker data
tickerData=yf.Ticker(tickerSymbol)
#get the historical prices
tickerDf=tickerData.history(period='id',start='2010-5-31',end='2020-5-31')
#Open High low volume stack splits
st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Closing Volume Chart
""")#Streamlit use mardown file
st.line_chart(tickerDf.Volume)
st.write("""
## Apple
""")
#define ticker volume
tickerSymbols='AAPL'
#define ticker data
tickerDatas=yf.Ticker(tickerSymbols)
#get the historical prices
tickerDfs=tickerDatas.history(period='id',start='2010-5-31',end='2020-5-31')
#Open High low volume stack splits
st.write("""
### Closing Price
""")
st.line_chart(tickerDfs.Close)
st.write("""
### Closing Volume Chart
""")#Streamlit use mardown file
st.line_chart(tickerDfs.Volume)

