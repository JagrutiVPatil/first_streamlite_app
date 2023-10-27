import pandas
import streamlit
streamlit.title('My Parents New Healthy Dinner')
my_text_file=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_text_file=my_text_file.set_index('Fruit')
Fruit_Selected=streamlit.multiselect("Pick Some fruits:", list(my_text_file.index),['Avocado','Strawberries'])
Fruit_to_show=my_text_file.loc[Fruit_Selected]
streamlit.dataframe(my_text_file)


