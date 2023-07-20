import webbrowser

import streamlit as st
import pandas as pd
from datetime import datetime

# streamlit run 1_home.py
if 'data' not in st.session_state:
    df_data = pd.read_csv('FIFA23_official_data.csv', index_col=0)
#    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
#    df_data = df_data[df_data['Value'] > 0],
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.write('# FIFA 23 OFICIAL DATASET!')
st.sidebar.markdown('Densenvolvido por Luzo')

btn = st.button('Acesse os dados no Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?resource=download')

st.markdown(
    """
    Informações aqui
    """
)