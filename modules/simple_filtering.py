import streamlit as st
import pandas as pd

from services.shopmonkey_api import fetch_data, get_auth


# Inicialização do estado da sessão para o token
if 'auth_token' not in st.session_state:
    st.session_state['auth_token'] = get_auth()
    

# Configuração da interface do Streamlit
st.title("Visualizador de Dados da API - Shopmonkey")

# Inputs de data
start_date = st.sidebar.date_input("Data Inicial")
end_date = st.sidebar.date_input("Data Final")
isinvoice = st.sidebar.multiselect("IsInvoice", options=['true', 'false'], max_selections=1)

# Botão para buscar dados
if st.sidebar.button("Buscar Dados"):
    isinvoice = isinvoice[0] if len(isinvoice) == 1 else None

    data = fetch_data(start_date, end_date, isinvoice)
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)