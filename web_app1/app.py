#Core Pkgs
import streamlit as st
st.set_page_config(page_title="NLP Web App", page_icon=":thumbsup:", layout="centered", initial_sidebar_state="auto")


# NLP Pkgs
import spacy
import neattext as nt
from textblob import TextBlob
from deep_translator import GoogleTranslator



from collections import Counter
import re

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud


def summarize_text(text, num_sentences=3):
    clean_text = re.sub('[^a-zA-z]', ' ', text).lower()

    words = clean_text.split()

    word_freq = Counter(words)

    print(word_freq.get)

    sorted_words = sorted(word_freq, key=word_freq.get, reverse=True)

    top_words = sorted_words[:num_sentences]

    summary = ' '.join(top_words)

    return summary

def text_analyzer(text):
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    allData = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_)) for token in doc]

    return allData

def main():
    """ NLP Web app With Streamlit"""

    title_template = """
<div style="background-color:blue; padding:8px;">
<h1 style="color:cyan">NLP Web App</h1>
</div>
"""
    st.markdown(title_template, unsafe_allow_html=True)

    subheader_template = """
<div style="background-color:cyan; padding:8px;">
<h3 style="color:blue">Powered by Streamlit</h1>
</div>
"""
    st.markdown(subheader_template,unsafe_allow_html=True)

    st.sidebar.image("web_app1/nlp.jpg", use_container_width =True)
    #st.title("NLP Web App")
    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu",activity)

    if choice == "Text Analysis":
        st.subheader("Text Analysis")
        st.write("")
        raw_text = st.text_area("Write Something", "Enter a text in English...", height=300)
        if st.button("Analyze"):
            if len(raw_text) == 0:
                st.warning("Enter a text")
            else:
                #blob = TextBlob(raw_text)
                st.info("Basic Function")

                col1, col2 = st.columns(2)

                with col1:
                    with st.expander("Basic Info"):
                        st.write("Text Stats")
                        word_desc = nt.TextFrame(raw_text).word_stats()
                        result_desc = {"Length of Text":word_desc['Length of Text'],
                                        "Num of Vowels":word_desc['Num of Vowels'],
                                        "Num of Consonants":word_desc['Num of Consonants'],
                                        "Num of Stopword:word_desc":word_desc['Num of Stopwords']}
                        st.write(result_desc)
                    with st.expander("Stopwords"):
                        st.success("Stopwords List")
                        stop_w = nt.TextExtractor(raw_text).extract_stopwords()
                        st.error(stop_w)

                with col2:
                    with st.expander("Processed Text"):
                        st.success("Stopwords Excluded Text")
                        processed_text = str(nt.TextFrame(raw_text).remove_stopwords())
                        st.write(processed_text)
                    with st.expander("Plot WordCloud"):
                        st.success("Wordcloud")
                        wordcloud = WordCloud().generate(processed_text)
                        fig = plt.figure(1, figsize=(20,10))
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis('off')
                        st.pyplot(fig)

                st.write("")
                st.write("")
                st.info("Advanced Features")

                col3, col4 = st.columns(2)

                with col3:
                    with st.expander("Tokens$Lemmas"):
                        st.write("T&K")
                        processed_text_mid = str(nt.TextFrame(raw_text).remove_stopwords())
                        processed_text_mid = str(nt.TextFrame(processed_text_mid).remove_puncts())
                        processed_text_fin = str(nt.TextFrame(processed_text_mid).remove_special_characters())
                        tandl = text_analyzer(processed_text_fin)
                        st.json(tandl)
                with col4:
                    with st.expander("Summarize"):
                        summary = summarize_text(raw_text)
                        st.success(summary)
    if choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        st.write("")
        st.write("")

        raw_text = st.text_area("Text to Analyse", "Enter a text here ...", height=200)
        if st.button("Evaluate"):
            if len(raw_text) == 0:
                st.warning("Enter a text...")
            else:
                blob = TextBlob(raw_text)
                blob = Text(raw_text)
                st.info("Sentiment Analysis")
                st.write(blob.sentiment)                
                st.write("")
    if choice == "Translation":
        st.subheader("Translation")
        st.write("")
        st.write("")
        raw_text = st.text_area("Original Text", "Write Something to be translated", height=200)
        if len(raw_text) < 3:
            st.warning("Please provide a text with at least 3 characters")
        else:
            target_lang = st.selectbox("Target a language", ["German", "Spanish", "Brazilian Portuguese", "French"])
            if target_lang == 'German':
                target_lang = 'de'
            elif target_lang == 'Spanish':
                target_lang = 'es'
            elif target_lang == 'Brazilian Portuguese':
                target_lang = 'pt'
            elif target_lang == 'French':
                target_lang = 'fr'
            if st.button("Translate"):
                translator = GoogleTranslator(source='auto', target=target_lang)
                translated_text = translator.translate(raw_text)
                st.write(translated_text)
    if choice == "About":
        st.subheader("About")
        st.write("")
        st.markdown("""
        ### NPL web App Made with Streamlit
        for info:
        - [streamlit](https://streamlit.io)
        """)      

if __name__ == '__main__':
    main()
    print(GoogleTranslator().get_supported_languages())
    