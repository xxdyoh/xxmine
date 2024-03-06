import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('main_data.csv')


st.sidebar.title('Pilih Tanggal dan Stasiun')


year = st.sidebar.selectbox('Pilih Tahun', options=df['year'].unique())


month = st.sidebar.selectbox('Pilih Bulan', options=df['month'].unique())

station = st.sidebar.selectbox('Pilih Stasiun', options=df['station'].unique())

filter = (df['year'] == year) & (df['month'] == month) & (df['station'] == station)

df_filtered = df[filter]

fig1 = px.line(df_filtered, x='day', y=['PM2.5', 'PM10'], title=f'Tren Konsentrasi partikel halus PM2.5 dan PM10 di Stasiun {station} pada Bulan {month} Tahun {year}')
st.plotly_chart(fig1)

fig2 = px.scatter(df_filtered, x='RAIN', y=['PM2.5', 'PM10'], title=f'Pengaruh hujan terhadap konsentrasi polutan di Stasiun {station} pada Bulan {month} Tahun {year}')
st.plotly_chart(fig2)

fig3 = px.box(df, x='station', y=['PM2.5', 'PM10'], title=f'Perbandingan Tingkat Polusi antar Stasiun pada Bulan {month} Tahun {year}')
st.plotly_chart(fig3)
