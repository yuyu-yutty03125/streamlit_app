import streamlit as st
import pandas as pd
import plotly.express as px

# ページ設定
st.set_page_config(
    page_title="売上高と失業率の関係",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# タイトルと導入文
st.title("📈 売上高と失業率の関係")
st.markdown("""
### 導入
経済活動において、雇用状況と産業の売上は密接に関連していると考えられますが、その関係は必ずしも明確ではありません。景気の変動、消費者行動、企業の投資判断、政府の経済政策など、複数の要因が両者に影響を及ぼすためです。
""")

# データの読み込みと前処理
df1 = pd.read_csv('サービス産業の売上高_全国_月_原.csv')
df2 = pd.read_csv('完全失業率_全国_月_季.csv')

df1 = df1[['時点', 'サービス産業計（売上高）【百万円】']]
df2 = df2[["時点", "（季節調整値）完全失業率（男女計）【%】"]]

df1 = df1[df1['時点'] >= '2013年1月']
df2 = df2[df2['時点'] >= '2013年1月']

df = pd.merge(df1, df2, on='時点', how='inner')
df.columns = ['時点', '売上高（百万円）', '失業率（%）']

# サイドバーで表示形式を選択
st.sidebar.header("表示形式の選択")
view_option = st.sidebar.radio(
    "表示形式を選んでください",
    ("📊 散布図", "📋 表")
)

# 相関係数の計算
corr = df['売上高（百万円）'].corr(df['失業率（%）'])

# メインコンテンツの表示
if view_option == "📊 散布図":
    st.subheader("散布図：売上高と失業率の関係")
    fig = px.scatter(
        df,
        x='失業率（%）',
        y='売上高（百万円）',
        title='売上高と失業率の関係',
        labels={
            '失業率（%）': '完全失業率（%）',
            '売上高（百万円）': 'サービス産業売上高（百万円）'
        },
        trendline='ols'
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**相関係数**: {corr:.3f}")

elif view_option == "📋 表":
    st.subheader("データ表：売上高と失業率")
    st.dataframe(df, use_container_width=True)

# 結果の解釈
st.markdown("""
### 結果の解釈
- **相関係数**が-0.347と負の値を示しており、失業率が上昇するにつれて売上高が減少する傾向が統計的に確認されました。
- これは、景気の悪化が雇用とサービス産業の売上に同時に影響を及ぼしている可能性を示しています。
- ただし、散布図にはばらつきも存在し、すべての時点で厳密な比例関係が成り立っているわけではありません。
""")
