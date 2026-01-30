import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Streamlitのグラフ表示')

df = pd.DataFrame(data=np.random.randint(0, 1000, (3, 6)),
                  index=['支店A', '支店B', '支店C'],
                  columns=['1月', '２月', '３月', '４月', '５月', '６月'])

st.header('1. 折れ線グラフの表示')
st.line_chart(df.T)

st.header('2. 棒グラフの表示')
st.bar_chart(df.T)

st.header('3. 面グラフの表示')
st.area_chart(df.T)

st.header('4. 散布図の表示')
df_sales_2023 = pd.read_csv('air_conditioner_sales_2023.csv', index_col='date')
st.scatter_chart(df_sales_2023, x='temp', y='sales')

st.header('5. 散布図の表示(Matplotlib)')
# 散布図の描画
plt.scatter(df_sales_2023['temp'], df_sales_2023['sales'], 
            s=50,          # マーカーのサイズ
            color='b',     # マーカーの色 'b'青色, 'r'赤色など
            marker='D',    # マーカーの種類 'o', 'x', 'D' など
            alpha=0.3      # 透明度
           )
# 散布図の装飾
plt.xlim(15.0, 40.0) # x軸の表示範囲
plt.ylim(300, 750)   # y軸の表示範囲
plt.title('Air Conditioner Sales vs Temparature 2023', fontsize=16)  # タイトル
plt.xlabel('Temparature (℃)', fontsize=16)                    # x軸ラベル
plt.ylabel('Sales (thousand $)', fontsize=16)                           # y軸ラベル
plt.grid(True)                  # 目盛線の表示
plt.tick_params(labelsize = 12) # 目盛線のラベルサイズ    
st.pyplot(plt.gcf())

st.header('6. 散布図の表示(Plotly)')
fig = px.scatter(df_sales_2023,
                 x='temp',
                 y='sales',
                 size='sales',
                 labels={'temp': 'Temperature (℃)', 'sales': 'Sales (thousand $)'}, 
                 title='Temp vs Sales')
st.plotly_chart(fig)

