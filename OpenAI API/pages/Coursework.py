# Installations and imports
#pip install streamlit
#pip install python-dateutil
#pip install "pyzmq==17.0.0" "ipykernel==4.8.2"

import streamlit as st
import openai
import os

# Main content
st.sidebar.success("Select a page above.")

st.title('AI and Big Data in Business Strategy')
st.header('A Course for the Future')

st.markdown(
    """
    Welcome to the Coursework page. Here is where you can talk with Alex about all things artificial intelligence. 
    Click into the text box below to begin learning!
    """
)

# Insert environmental variable that links to your OpenAI Key (configured on your computer)
openai.api_key = os.getenv('OPENAI_API_KEY')

# User input
user_input = st.text_input('What is your query?')

# AI response
if st.button('Submit here.'):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.8,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    st.write('As a reminder, your query was:', user_input)
    st.write("Alex's response:", response.choices[0].text)