import os
import streamlit as st
import langchain_google_genai
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage,SystemMessage


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.title('AI Advanced Translator ')
st.subheader('Learn Basic to Pro in Multi Languages')
choose_language=st.selectbox('select target language',['Telugu','Hindi','Tamil','Spanish','China','German'])
user_input =st.text_input('Type you Message')
if user_input:
    messages=[SystemMessage('transalte the sentences in telugu'),
         HumanMessage(content=f'you are a expert in translator .Trasnsalte the all the sentence into {choose_language}.Only provide the transaltion wuthout extra chat')]
    
    model=init_chat_model('google_genai:gemini-2.5-flash')
    with st.spinner('Transalting....'):
        response=model.invoke(messages).content
    st.success(f'translation...{choose_language}:{response}')