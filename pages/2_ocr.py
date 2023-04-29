import streamlit as st
from streamlit_drawable_canvas import st_canvas

import pandas
import numpy

import json
import requests

from PIL import Image

canvas_result = st_canvas(background_color="#FFFFFF")

API_TOKEN = st.secrets['hf_token']

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-small-handwritten"


@st.cache_data
def query(data):
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data, 'RGBA')
    img.save('test.png', 'PNG')

    with open('test.png', "rb") as f:
        data = f.read()

    f = query(data)
    f
