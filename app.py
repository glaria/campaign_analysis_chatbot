import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Chatbot App 👋")

st.markdown(
    """
    Language model:  LaMini-Flan-T5-248M
    See: https://github.com/mbzuai-nlp/lamini-lm https://github.com/jncraton/languagemodels

    **👈 
    
    ### Documentation should go here
"""
)

url = 'Data_Load'
#st.write("check out this [link](%s)" % url)
st.markdown("Go to the [Data Load Page](%s)" % url)