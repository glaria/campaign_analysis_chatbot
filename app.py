import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Campaign Analysis App 👋")

st.markdown(
    """
    Optimized version of the app:

    - Advanced anaytics focuses on finding best and worst subsets. 
    - Basis lgbm simplified

    **👈 
    
    ### Documentation should go in here
"""
)

url = 'Data_Load'
#st.write("check out this [link](%s)" % url)
st.markdown("Go to the [Data Load Page](%s)" % url)