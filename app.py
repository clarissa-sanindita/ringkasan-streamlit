import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyCH_dRU5svjGhHdBKbiczs_KauUztUGlnI')

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.3, 
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

text_to_summarize = st.text_area("Enter the text you want to summarize:")
add_promt = "Make a summary"

prompt =add_promt + " " + text_to_summarize

if st.button('Generate Summary'):
    response = genai.generate_text(
        **defaults,
        prompt=prompt  
    )
    st.write(response.result)

