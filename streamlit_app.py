import pandas
import streamlit
import requests
fruitvicy_response=requests.get('https://fruityvice.com/api/fruit/watermelon')
streamlit.text(fruitvicy_response)
