import streamlit as st
import requests

data = requests.get("https://api.nasa.gov/planetary/apod?"
                    "api_key=9laIEqDTIDyJVuVm1mDtO1m3E4sEXc5f0jkcPkM8")
content = data.json()
print(content['media_type'])
st.header(content['title'])
if content['media_type'] == "video":
    st.video(content['url'])
elif content['media_type'] == "image":
    st.image(content['url'])
st.write(content['explanation'])

