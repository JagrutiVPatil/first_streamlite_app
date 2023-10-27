import pandas
import streamlit
import requests
fruit_choice=streamlit.text_input('what is your favourite fruit','Kiwi')
streamlit.write('Use entered',fruit_choice)
fruitvicy_response=requests.get("https://fruityvice.com/api/fruit/watermelon" +fruit_choice)
streamlit.text(fruitvicy_response)
streamlit.text(fruitvicy_response.json())
fruitvicy_normalize=pandas.json_normalize(fruitvicy_response.json())
streamlit.dataframe(fruitvicy_normalize)

