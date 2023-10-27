import pandas
import streamlit
import requests
streamlit.header('Fruitvicy header')
fruitvicy_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvicy_response)
streamlit.text(fruitvicy_response.json())
#Take a json version of response and normaliz eit
fruitvicy_normalize=pandas.json_normalize(fruivicy_response.json())
#output it to screen as table
streamlit.dataframe(fruitvicy_normalize)

