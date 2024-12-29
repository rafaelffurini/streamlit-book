import streamlit as st

st.title("Streamlit Basics")

#st.header("This is a header")
#st.subheader("This is a subheader")
#st.text("This is a simple text")
#st.write("This is a write dimension")

#st.markdown("[Streamlit](https://www.streamlit.io)")

#html_page = """
#<div style="background-color:blue;padding:50px">
#<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
#</div>
#"""
#st.markdown(html_page, unsafe_allow_html=True)

#st.success("Success!")
#st.info("Information")
#st.warning("This is a warning!")
#st.error("This is an error!")
#st.video("https://www.youtube.com/watch?v=q2EqJW8VzJo")

#st.header("Widgets")

#if st.button("Play"):
#    st.text("Hello World!")


#if st.checkbox("Checkbox"):
#      st.text("Checkbox selected")


#radio_but = st.radio("Your Selection", ["A", "B"])
#if radio_but == "A":
#      st.info("You selected A")
#else:
#      st.info("You selected B")

#city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

#occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

#name = st.text_input("Your Name", "Write something…")

#st.text(name)

#age = st.number_input("Input a number")

#message = st.text_area("Your Message", "Write something...")

#select_val = st.slider("Select a Value", 1, 10)

#if st.button("Balloons"):
#      st.balloons()
      
st.header("Dataframes and Tables")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time

df = pd.read_csv("auto.csv")

st.dataframe(df.head(10))

st.area_chart(df[['mpg','cylinders']])
st.bar_chart(df[['mpg','cylinders']].head(20))
st.line_chart(df[['mpg','cylinders']].head(20))


fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[['mpg', 'cylinders', 'displacement']].corr(), annot=True)

st.pyplot(fig)

today = st.date_input("Today is ", datetime.datetime.now())

hour = st.time_input("The time is ", datetime.time(12,30))

data = {"name":"Jhon", "surname":"Wick"}
st.json(data)

st.code("import pandas as pd")

my_bar = st.progress(0)
for value in range(100):
      time.sleep(0.01)
      my_bar.progress(value+1)

with st.spinner("Please wait ..."):
      time.sleep(10)
st.success("Done!")

