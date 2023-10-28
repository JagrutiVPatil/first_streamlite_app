import streamlit
import pandas
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("Fruit LOad List Contains")
streamlit.dataframe(my_data_row)
streamlit.title('My Parents New Healthy Dinner')
my_text_file=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_text_file=my_text_file.set_index('Fruit')
Fruit_Selected=streamlit.multiselect("Pick Some fruits:", list(my_text_file.index),['Avocado','Strawberries'])
Fruit_to_show=my_text_file.loc[Fruit_Selected]
streamlit.dataframe(Fruit_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/kiwi")
streamlit.text(fruityvice_response)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

