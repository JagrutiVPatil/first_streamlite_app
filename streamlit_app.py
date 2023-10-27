import streamlit
import pandas
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

