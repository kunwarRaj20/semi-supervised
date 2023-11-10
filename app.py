import streamlit as st
import pandas as pd
import joblib
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Sentiment Analysis", layout="wide")

with st.container():
    st.title("Sentiment Analysis")
    st.subheader("User Input Text Analysis")
    st.text("Analyzing text data given by the user and find sentiments within it.")
    st.text("")
    st.text("Sample text to use")
    st.text("Positive - I can play video games and listen to my favorite music")
    st.text("Neutral - Liked Songs display songs sort recently added")
    st.text("Negative - Just updated the app now it s not opening for me it keeps crashing")

with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

cs = joblib.load('senitment_analysis.pkl')
vector = joblib.load('vector.pkl')

def predict_sentiment(input_data):
    
    textdata = vector.transform([input_data])
    prediction=cs.predict(textdata)
    response = ''
    if prediction == 'positive':
        response = 'Positive'
    elif prediction == 'neutral':
        response = 'Neutral'
    elif prediction == 'negative':
        response = 'Negative'
    return response

def main():
    
    userText = st.text_input('User Input', placeholder='Input text HERE')
    st.text("")
    
    result = ""

    if st.button("Predict"):
        result=predict_sentiment(userText)
        st.success(result)

    if st.button("Reset"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


if __name__ == '__main__':
        main ()