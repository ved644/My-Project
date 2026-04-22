import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title='Smart Water Monitoring Dashboard', layout='wide')

st.title('AI Smart Water Monitoring Dashboard')
st.caption('IoT-enabled Water Leakage, Theft Detection & Predictive Analytics System')

flow = np.random.randint(75, 110)
pressure = np.random.randint(40, 65)
leak = 'Detected' if pressure < 48 else 'Normal'
theft = 'Suspicious' if flow > 98 else 'Clear'

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric('Live Flow Data', f'{flow} L/min')
c2.metric('Pressure', f'{pressure} PSI')
c3.metric('Leakage Warning', leak)
c4.metric('Theft Alert', theft)
c5.metric('Connected Nodes', '24 Online')

hours = list(range(12))
df = pd.DataFrame({
 'time':[f'{h}:00' for h in hours],
 'flow':[70 + (h%6)*5 for h in hours],
 'pressure':[45 + (h%5)*3 for h in hours]
})

col1,col2 = st.columns(2)
with col1:
 st.subheader('Flow & Pressure Trends')
 fig = go.Figure()
 fig.add_trace(go.Scatter(x=df['time'], y=df['flow'], mode='lines+markers', name='Flow'))
 fig.add_trace(go.Scatter(x=df['time'], y=df['pressure'], mode='lines+markers', name='Pressure'))
 st.plotly_chart(fig, use_container_width=True)
with col2:
 st.subheader('Area-wise Usage')
 area = pd.DataFrame({'Area':['Zone A','Zone B','Zone C','Zone D'],'Usage':[320,280,410,190]})
 fig2 = px.bar(area, x='Area', y='Usage')
 st.plotly_chart(fig2, use_container_width=True)

st.subheader('Map-based Monitoring')
map_df = pd.DataFrame({'lat':[23.18,23.20,23.16,23.22],'lon':[77.41,77.43,77.46,77.39]})
st.map(map_df)

st.subheader('Recent Alerts & AI Recommendations')
st.warning('Pressure drop in Zone B pipeline')
st.error('Unusual night consumption in Zone D')
st.info('Recommend inspection for Zone B valve in next 48 hrs')
