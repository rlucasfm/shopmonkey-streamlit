from dotenv import load_dotenv
import json
import requests
import os
import streamlit as st
import pandas as pd

load_dotenv()

# Inicialização do estado da sessão para o token
if 'auth_token' not in st.session_state:
    st.session_state['auth_token'] = None

def get_auth():
    auth_url = "https://api.shopmonkey.io/v2/token"
    payload = {
        "publicKey": os.getenv("SHOPMONKEY_PUBLIC_KEY"),
        "privateKey": os.getenv("SHOPMONKEY_PRIVATE_KEY")
    }

    response = requests.post(auth_url, json=payload)
    if response.status_code == 201:
        return response.text
    else:
        print("Error: ", response.text)
        return None

# Função para buscar dados da API
def fetch_data(start_date, end_date, isinvoice=None):
    url = "https://api.shopmonkey.io/v2/orders"
    headers = {
        "Authorization": f"Bearer {st.session_state['auth_token']}"
    }
    params = {
        "limit": 100,
        "creationDateStart": start_date,
        "creationDateEnd": end_date
    }

    if isinvoice is not None: params["isInvoice"] = isinvoice

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        token = get_auth()
        st.session_state['auth_token'] = token
        fetch_data(start_date, end_date)
    else:
        st.error("Erro ao buscar dados da API")
        return None

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