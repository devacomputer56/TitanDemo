#This is code of Titan App.
#Developed by DeVa Quantum Genesis.
#Welcome to Titan side.

pip install streamlit google-generativeai google-ai.generativelanguage

import streamlit as st
import google.generativeai as gemini
import google.ai.generativelanguage as glm

genai.configure(api_key="My API")

#Title

st.set_page_config(
    page_title="Titan Ultra"
)

st.title("Titan Ultra")
st.subheader("How can I help you?")

#Start Session
if "chat_session"not in st.sessiion_state :
    #Loading Titan Ultra Model
    fine_tuned_model = genai.GenerativeModel.from_pretrained("My Link")

st.session_state["chat_session"] =
fine_tuned_model.start_chat(history=[
    glm.Content(role="user",
                parts=[glm.Part(text="あなたはTitanという大規模言語モデルです。")])

    glm.Content(role="model",
                parts=[glm.Part(text="かしこまりました")])
])
st.session_state["chat_history"] = []


for massage in
st.session_state["chat_history"]:
    with
    st.chat_massage(massage["role"]):
        st.markdown(massage["content"])

if prompt := st.chat_input ("さまざまなことを尋ねてみてください"):

    with st.chat_massage("user"):
        st.markdown(prompt)

st.session_state["chat_history"].
append({"role":"user","content":prompt})

response = st.session_state["chat_session"].send_massage(prompt)

with st.chat_massage("assistant"):
    st.markdown(response.text)

st.session_state["chat_history"].append({"role":"assistant","content":response.text})
