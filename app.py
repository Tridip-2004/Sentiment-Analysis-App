import streamlit as st
import joblib
import re

st.set_page_config(page_title="Sentiment Predictor", page_icon="🧠")

st.title("🧠 Sentiment Predictor")
st.write("Predict whether a sentence is **Positive** or **Negative**.")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("sentiment_model_v2.joblib")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"http\S+|[^a-z\s]", " ", text)
    return " ".join(text.split())

try:
    model = load_model()

    text = st.text_area("Enter a sentence:", placeholder="e.g. I love this product!")

    if st.button("Predict"):
        if text.strip():
            clean = preprocess(text)
            pred  = model.predict([clean])[0]
            proba = model.predict_proba([clean])[0]
            conf  = max(proba) * 100

            if pred == 1:
                st.success(f"✅ **POSITIVE** — {conf:.1f}% confidence")
            else:
                st.error(f"❌ **NEGATIVE** — {conf:.1f}% confidence")
        else:
            st.warning("Please enter a sentence.")

except FileNotFoundError:
    st.error("⚠️ `sentiment_model.joblib` not found. Place it in the same folder and restart.")