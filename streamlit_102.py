import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('広告費と売上')

df = pd.read_csv('../files/files/ad_expense_sales.csv')


with st.sidebar:
    st.header('抽出条件')

    selected_cats = st.multiselect(
        '製品カテゴリを選択',
        df['prod_category'].unique(),
        default=df['prod_category'].unique()
    )
    selected_media = st.selectbox(
        '広告媒体を選択',
        df['media'].unique()
    )
    group_col = st.selectbox(
        '分析軸を選択',
        ['sex', 'age', 'season']
    )
    view_option = st.radio(
        '表示形式を選択',
        ['表', 'グラフ']
    )


df_filtered = df[df['prod_category'].isin(selected_cats)]
df_filtered = df_filtered[df_filtered['media'] == selected_media]


summary = (
    df_filtered
    .groupby(group_col)[['ad_expense', 'sales']] #確認
    .sum()
)


st.write('単位：万円')

if view_option == '表':
    st.dataframe(summary, width=800)

elif view_option == 'グラフ':
    st.bar_chart(summary)