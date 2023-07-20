import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="Luzo",
    layout="wide"
)

df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[df_data['Club'] == club].set_index('Name')

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"{club}")
df_filtered