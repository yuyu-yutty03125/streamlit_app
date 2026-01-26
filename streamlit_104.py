import streamlit as st
import pandas as pd

st.title('広告費と売上')

df = pd.read_csv('../files/files/ad_expense_sales.csv')

with st.sidebar:
    selected_cats = st.multiselect(
        '製品カテゴリを選択してください（複数選択可）',
        df['prod_category'].unique()
    )

    selected_media = st.selectbox(
        '広告媒体を選択してください',
        df['media'].unique()
    )

    axis_dict = {
        '性別': 'sex',
        '年齢層': 'age',
        '季節': 'season'
    }

    axis_label = st.selectbox(
        '分析軸を選択してください',
        list(axis_dict.keys())
    )

    option = st.radio(
        '表示形式を選択してください',
        ['表', 'グラフ']
    )

df = df[df['prod_category'].isin(selected_cats)]
df = df[df['media'] == selected_media]

group_col = axis_dict[axis_label]

df = df.groupby(group_col)[['sales', 'ad_expense']].sum()

df.rename(columns={
    'sales': '売上',
    'ad_expense': '広告費'
}, inplace=True)

df.index.name = axis_label

st.write('単位：万円')

if option == '表':
    st.dataframe(df, width=800, height=220)

elif option == 'グラフ':
    st.line_chart(df)
