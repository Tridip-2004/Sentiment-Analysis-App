# Sentiment-Analysis-App
A simple yet powerful Sentiment Analysis Web App built with Streamlit that predicts whether a sentence expresses a positive or negative sentiment using Machine Learning. The backend model is trained using sklearn, and NLP tasks are handled using nltk, while numpy and pandas support data operations. The trained model is saved using pickle for fast and efficient loading.

# 📱 Live Web App
https://sentiment-analysis-app-jrvpjtw2ajshwdqqmng6is.streamlit.app/


# Features
📝 Predicts sentiment of input sentence (Positive / Negative)

🧹 Text preprocessing with NLTK (tokenization, stopword removal)

⚙️ ML Model trained using Naive Bayes from scikit-learn

💾 Model saved and loaded using Pickle

🌐 Interactive web app built with Streamlit

# Tech Stack
Programming	Language - Python 3.x

Data Handling -	numpy , pandas

Data Visualization - Matplotlib , Seaborn

ML model building -scikit-learn

Model I/O	- joblib

Web App	Streamlit 

Deploy on Streamlit

# How It Works

1.User inputs a sentence via the web interface.

2.Text is cleaned and vectorized using preloaded CountVectorizer or TfidfVectorizer.

3.Trained Naive Bayes model classifies the sentiment.

4.App displays if the sentiment is Positive or Negative.

# License
This project is licensed under the MIT License.


