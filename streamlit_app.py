import pandas
import streamlit
fruit_choice=streamlit.text_input('what is your favourite fruit','Kiwi')
streamlit.write('Use entered',fruit_choice)
import requests
fruitvicy_response=requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
