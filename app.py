import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

st.title("AI-Powered Meeting Intelligence System")

meeting = st.text_area("Paste Meeting Transcript")

if st.button("Analyze Meeting"):
    prompt = f"""
    Analyze the following meeting transcript.
    Give:
    1. Meeting Summary
    2. Action Items
    3. Key Decisions

    Transcript:
    {meeting}
    """

    response = llm.invoke(prompt)

    st.subheader("AI Output")
    st.write(response.content)