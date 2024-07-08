from llama_index.llms.openai import OpenAI
from llama_index.experimental.query_engine import PandasQueryEngine
import pandas as pd
import streamlit as st

def load_csv():
    uploaded_file = st.sidebar.file_uploader("Carregar arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        # DataFrame de exemplo caso nenhum arquivo seja carregado
        return pd.DataFrame(
            {
                "city": ["Toronto", "Tokyo", "Berlin"],
                "population": [2930000, 13960000, 3645000],
            }
        )

# Carregar o DataFrame
df = load_csv()

# Exibir o DataFrame carregado
st.sidebar.write("DataFrame carregado:")
st.sidebar.write(df)

llm = OpenAI()
query_engine = PandasQueryEngine(llm=llm, df=df, verbose=True)

st.title("Chat com PandasQueryEngine")

user_query = st.text_input("Faça sua pergunta:")

if st.button("Buscar Dados"):
    if user_query:
        response = query_engine.query(user_query)
        st.write(response.response)
    else:
        st.write("Faça uma pergunta sobre os dados")
