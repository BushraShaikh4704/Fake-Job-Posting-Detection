
import streamlit as st
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("Fake Job Posting Detection")

user_input = st.text_area("Enter Job Description")

if st.button("Predict"):
    text_vector = vectorizer.transform([user_input])
    prediction = model.predict(text_vector)[0]

    if prediction == 1:
        st.error("🚨 Fake Job")
    else:
        st.success("✅ Real Job")
