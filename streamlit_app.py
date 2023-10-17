import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging


# Logging setup
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


@st.cache(allow_output_mutation=True)
def load_model():
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    tokenizer.add_special_tokens({'additional_special_tokens': ['[SENTIMENT]', '[CATEGORY]']})
    model_path = "final-model"
    model = DistilBertForSequenceClassification.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model()

# Streamlit UI (Title and Input)
st.title('Bitcoin Sentiment Analysis App')
text = st.text_area("Enter Text for Analysis:")

# Prediction
if st.button('Analyze'):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    _, prediction = torch.max(probs, dim=1)

    # Display sentiment prediction
    sentiment_map = {0: "Negative 😞", 1: "Neutral 😐", 2: "Positive 😃"}
    sentiment = sentiment_map[prediction.item()]
    st.write(f'Sentiment: {sentiment}')
    
    # Log user interaction
    logging.info(f"User Input: {text} | Model Prediction: {sentiment}")

    # Sentiment Distribution Pie Chart and Word Cloud
    st.subheader("Sentiment Distribution & Word Cloud")

    # Create two columns for pie chart and word cloud
    col1, col2 = st.columns(2)

    # Pie chart in first column
    with col1:
        sentiment_labels = ['Negative', 'Neutral', 'Positive']
        probs_data = probs[0].detach().numpy()

        fig, ax1 = plt.subplots()

        wedges, texts = ax1.pie(probs_data, startangle=90)
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig.gca().add_artist(centre_circle)
        ax1.legend(wedges, sentiment_labels, title="Sentiments", loc="best")
        ax1.axis('equal')

        st.pyplot(fig)

        st.write(f"Negative sentiment: {probs_data[0]:.2f}%")
        st.write(f"Neutral sentiment: {probs_data[1]:.2f}%")
        st.write(f"Positive sentiment: {probs_data[2]:.2f}%")

    # Word Cloud in second column
    with col2:
        wordcloud = WordCloud(width=800, height=400, background_color ='white', stopwords = set(['the', 'and', 'to'])).generate(text)
        fig3, ax3 = plt.subplots(figsize=(10,7))
        ax3.imshow(wordcloud, interpolation='bilinear')
        ax3.axis('off')
        st.pyplot(fig3)    

# Sidebar Info
st.sidebar.title("About App")
st.sidebar.info("This is a sentiment analysis app using a fine-tuned DistilBERT model.")
st.sidebar.title("Model Predictions")
st.sidebar.write("0: Negative, 1: Neutral, 2: Positive")
  

# Additional Sidebar Features
st.sidebar.subheader("Model Details")
st.sidebar.write("Model Type: DistilBERT")
st.sidebar.write("Training Data: Bitcoin Reddit Comments")
st.sidebar.write("Accuracy: 91% (Train), 88% (Validation)")
st.sidebar.markdown("[More about BERT and its variants](https://arxiv.org/abs/1810.04805)")
st.sidebar.markdown("[Some BERT illustrations](https://jalammar.github.io/illustrated-bert/)")


# Sidebar Info and Feedback Form
st.sidebar.subheader("Feedback")
feedback = st.sidebar.text_area("Please leave your feedback here:")
if st.sidebar.button("Submit Feedback"):
    logging.info(f"User Feedback: {feedback}")
    st.sidebar.write("Thank you for your feedback!")

