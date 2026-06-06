# import the packages
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


#set the api key for both gemieni api key & langsmith apikey

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGGRAPH_API_KEY = os.getenv("LANGGRAPH_API_KEY")


#PROMPT TEMPLATE

prompt =ChatPromptTemplate.from_messages([('system','you are a chatbot which assistant to the world about the latest news'),
 'human','{question}' ])

st.title('Gemini chat model with langchain created by Someshwar')
input_text=st.text_input('How may i help you today ? if you write one word the i am hallucinate')

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key=GOOGLE_API_KEY,temperature=1,max_output_tokens=1000)

output_parser = StrOutputParser()

chain= prompt | llm | output_parser

if input_text:
    with st.spinner('Generating response...'):
        try:
            response = chain.invoke({"question": input_text})
            st.success('Response generated successfully!')
            st.write(response)
        except Exception as e:
            st.error(f'An error occurred: {e}')