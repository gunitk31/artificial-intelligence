import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
import streamlit as st


st.title('NIFTY 50 Stock Price Data Analysis & Visualization')
st.write('This project is about NIFTY 50 Stock Price Data Analysis & Visualization. \
         The dataset is taken from Yahoo Finance. \
         The dataset contains the stock price data of NIFTY 50 companies from 2000 to 2021. \
         The dataset contains the following columns: \
         Date, Open, High, Low, Close, Adj Close, Volume, Symbol (Company Name).')

df = pd.read_csv(os.getcwd() + "\\..\\data\\NIFTY50_clean.csv")
df.head()

companies = df['Symbol'].unique()

company = st.selectbox('Select Company', companies)
st.write(f'You selected {company}')

st.line_chart(df[df['Symbol'] == company.strip()]['Open_scaled'])
st.line_chart(df[df['Symbol'] == company.strip()]['Close_scaled'])