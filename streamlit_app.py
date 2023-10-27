import pandas
import streamlit
streamlit.title('My Parents New Healthy Dinner')
my_text_file=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick Some fruits:", list(my_text_file.index))
streamlit.dataframe(my_text_file)


