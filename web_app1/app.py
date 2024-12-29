#Core Pkgs
import streamlit as st 

# NLP Pkgs
import spacy
import neattext as nt
from textblob import TextBlob

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud

def main():
    """ NLP Web app With Streamlit"""

    st.title("NLP Web App")
    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu",activity)
if __name__ == '__main__':
    main()