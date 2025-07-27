import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
import numpy as np

# Load Model & Vectorizer
model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Download stopwords (only once)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

# Preprocessing function (no `re` used)
def clean_text(text):
    text = text.lower()
    words = text.split()
    cleaned = []
    for word in words:
        word = word.strip(''.join(punctuations))
        if word.isalpha() and word not in stop_words:
            cleaned.append(word)
    return ' '.join(cleaned)

# Streamlit UI
st.title(" Sentiment Analysis App")
st.write("Enter a sentence and check whether it's Positive or Negative.")

user_input = st.text_area("Enter Text Below:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        if prediction == 1:
            st.success(f"🙂 Positive Sentiment ")
        else:
            st.error(f"🙁Negative Sentiment ")



st.markdown("---")
st.caption("Built using Scikit-learn & Streamlit")
