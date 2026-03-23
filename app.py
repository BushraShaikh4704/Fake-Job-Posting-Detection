import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Fake Job Detector", page_icon="🔍")

# Load model and vectorizer
@st.cache_resource
def load_models():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_models()

# Title and description
st.title("🔍 Fake Job Posting Detection")
st.write("Enter a job description below to check whether it is **Real or Fake**.")

# Text input
user_input = st.text_area("📝 Job Description", height=200)

# Example button
if st.button("✨ Try Example"):
    example_text = "Earn money from home, no experience required, click here now!"
    st.session_state["example"] = example_text
    st.write("Example loaded below 👇")
    user_input = example_text
    st.text_area("📝 Job Description", value=user_input, height=200)

# Prediction button
if st.button("🔍 Predict"):

    if user_input.strip() == "":
        st.warning("⚠ Please enter a job description first.")
    else:
        text_vector = vectorizer.transform([user_input])
        prediction = model.predict(text_vector)[0]

        st.subheader("Result:")

        if prediction == 1:
            st.error("🚨 This looks like a **FAKE job posting!**")
        else:
            st.success("✅ This looks like a **REAL job posting!**")

# Footer
st.markdown("---")
st.markdown("💡 Built using NLP & Machine Learning with Streamlit")