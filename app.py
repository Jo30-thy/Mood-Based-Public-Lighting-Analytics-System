import streamlit as st
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Load mood rules
with open("mood_rules.json", "r") as f:
    mood_rules = json.load(f)

# Load lighting rules
with open("lighting_rules.json", "r") as f:
    lighting_rules = json.load(f)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit interface
st.set_page_config(page_title="Mood-Based Public Lighting", layout="centered")
st.title("💡 Mood-Based Public Lighting Analytics")
st.write("Enter a message or comment to detect the mood and suggest appropriate lighting.")

# User Input
user_input = st.text_input("Your message:")

# Analyze when input is entered
if user_input:
    score = analyzer.polarity_scores(user_input)["compound"]

    # Determine mood
    mood = "neutral"  # default
    for label, rule in mood_rules.items():
        if rule["min"] <= score <= rule["max"]:
            mood = label
            break

    # Lighting color
    lighting = lighting_rules.get(mood, "White")

    # Show Results
    st.markdown(f"### Mood Detected: *{mood.upper()}*")
    st.markdown(f"### Suggested Light Color: *{lighting}*")

    # Mood emojis
    emojis = {
        "happy": "😊",
        "neutral": "😐",
        "sad": "😢"
    }
    st.markdown(f"### Mood Emoji: {emojis.get(mood, '😐')}")