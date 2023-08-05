import streamlit as st
import languagemodels as lm
import re

st.title("Chatbot")


#st.write(st.session_state.corpus)

#st.write(st.session_state.reference_dict)


corpus = st.session_state.corpus

reference_dict= st.session_state.reference_dict

lm.set_max_ram('4gb')
#lm.store_doc(lm.get_wiki("Planet Saturn"))
#lm.store_doc('The KPI acceptors has an uplift_value of *xgfw|a3|23')
#lm.store_doc('The KPI vgtr has an uplift of 45')
lm.store_doc(corpus)
#st.write(lm.models.get_model_name('instruct'))

def check_string(s): #check if a string contains the special characters of the keys defined
    if re.search(r'\*xgfw[^|]*\|[^|]*\|', s):
        return True
    else:
        return False

def assist(question):
    
    context = lm.get_doc_context(question)#.replace(": ", " - ")

    return lm.do(f"Answer using context: {context} Question: {question}")

def process_response(response):
    if check_string(response):
        key_d = re.search(r'\*xgfw\|([^|]*)\|', response).group(1) 
        return reference_dict[key_d] 
    else:
        return ('0', response)

if "messages" not in st.session_state:
    st.session_state.messages = []

#the content is different for the assistant because we need to know the data type of the answer to show it correctly
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["content"][0] == '0' and message["role"] == 'assistant':
            st.markdown(message["content"][1]) 
        elif message["content"][0] == 'fig' and message["role"] == 'assistant':
            st.plotly_chart(message["content"][1])
        elif (message["content"][0] == 'table' or message["content"][0] == 'list') and message["role"] == 'assistant':
            st.write(message["content"][1])
        else:
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        #st.write(prompt)
        message_placeholder = st.empty()
        full_response = ""
        #st.write(st.session_state.messages)
        response = assist(prompt)
        if process_response(response)[0] == '0':
            st.write(process_response(response)[1]) 
        elif process_response(response)[0] == 'fig':
            st.plotly_chart(process_response(response)[1])
        elif process_response(response)[0] == 'table' or  process_response(response)[0] == 'list':
            st.write(process_response(response)[1])
        print(response)
        full_response += response

        st.session_state.messages.append({"role": "assistant", "content": process_response(response)})
        #message_placeholder.markdown(full_response + "▌")
        #message_placeholder.markdown(full_response)
    #st.session_state.messages.append({"role": "assistant", "content": full_response})