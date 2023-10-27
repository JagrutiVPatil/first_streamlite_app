import pandas
import streamlit
import requests
streamlit.header('Fruitvicy header')
fruitvicy_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvicy_response)
streamlit.text(fruitvicy_response.json())
fruitvicy_normalize=pandas.json_normalize(fruitvicy_response.json())
streamlit.dataframe(fruitvicy_normalize)

