import streamlit as st

simple_filtering_page = st.Page("services/simple_filtering.py", title="Filtro Simples", icon=":material/add_circle:")
chat_data_page = st.Page("services/chat_with_data.py", title="Chat with data", icon=":material/delete:")

pg = st.navigation([simple_filtering_page, chat_data_page])
st.set_page_config(page_title="Shopmonkey API AI", page_icon=":material/edit:")
pg.run()