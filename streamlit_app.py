import pandas
import streamlit
import requests
streamlit.header('Fruitvicy header')
fruitvicy_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvicy_response)
streamlit.text(fruitvicy_response.json())
