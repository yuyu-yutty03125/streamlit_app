import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('広告費と売上')

df = pd.read_csv('../files/files/ad_expense_sales.csv')

with st.sidebar:
    products = st.multiselect('製品を選択を選択してください（複数選択可）',
                            df['Products'].unique())
    advertising = st.selectbox('年を指定',
                           min_value=df['年'].min(),
                           max_value=df['年'].max(),
                           value=df['年'].min(),
                           step=1)
    color = st.selectbox('色を選択',
                        sex=df['性別'].min(),
                        age=df['年齢層'].max(),
                        seasen=df['季節'].min(),
                        step=1)
