import streamlit as st

closing_data_page = st.Page("modules/closing_data.py", title="Fechamento do Dia", icon=":material/add_circle:")
simple_filtering_page = st.Page("modules/simple_filtering.py", title="Filtro Simples", icon=":material/add_circle:")
chat_data_page = st.Page("modules/chat_with_data.py", title="Chat with data", icon=":material/delete:")

pg = st.navigation([closing_data_page, simple_filtering_page, chat_data_page])
st.set_page_config(page_title="Shopmonkey API AI", page_icon=":material/edit:")
pg.run()