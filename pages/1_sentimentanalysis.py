import requests
import json
import streamlit as st
import pandas as pd
import numpy as np

st.title('Sentimental Analysis')

API_TOKEN = st.secrets['hf_token']


headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"


txt = st.text_input("Type sentimental analysis here!")


@st.cache_data
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query({"inputs": txt})

data
