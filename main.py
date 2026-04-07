import streamlit as st
import requests
import os
from dotenv import load_dotenv

#load env variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Call the API 
response = requests.get(url)
data = response.json()

#UI
st.title("Nasa Astronomy Picture of the Day")

#Image
st.image(data["url"])

#Description
st.write("Explination")