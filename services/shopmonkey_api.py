from dotenv import load_dotenv
import requests
import os
import streamlit as st

load_dotenv()

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
        fetch_data(start_date, end_date, isinvoice)
    else:
        st.error("Erro ao buscar dados da API")
        return None