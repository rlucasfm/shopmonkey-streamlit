from llama_index.llms.openai import OpenAI
from llama_index.llms.lmstudio import LMStudio
from llama_index.experimental.query_engine import PandasQueryEngine
import pandas as pd
import streamlit as st

llm = OpenAI()
# llm = LMStudio(
#     model_name="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
#     base_url="http://localhost:1234/v1",
#     api_key="lm-studio",
#     temperature=0.7,
# )


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

query_engine = PandasQueryEngine(llm=llm, df=df, verbose=True)

st.title("Chat com PandasQueryEngine")

user_query = st.text_input("Faça sua pergunta:")

if st.button("Buscar Dados"):
    if user_query:
        response = query_engine.query(user_query)
        st.write(response.response)
    else:
        st.write("Faça uma pergunta sobre os dados")
