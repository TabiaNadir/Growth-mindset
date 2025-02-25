import streamlit as st
import random

challenges =[
    "Think of a past failure and write what you learned from it.",
    "Try something new today that pushes you out of your comfort zone.",
    "Replace a negative thought with a positive one.",
    "Ask for feedback on something you're working on and apply it.",
    "Teach someone something new and learn from their perspective.",
]

quotes =[
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Your only limit is your mind.",
    "Difficulties in life are intended to make us better, not bitter.",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
]
st.title ("🚀 Growyh Mindset Challenge")

todays_challenge = random.choice(challenges)
st.header("📌 Today's Callenge")
st.write(todays_challenge)

st.subheader("📝 Your Reflection")
reflection = st.text_area("Write about your experience with today's challenge:")
if st.button("Save Reflection"):
    if reflection:
        st.success("✅ Your reflection has been saved!")
    else:
        st.warning("⚠️ Please write something before saving.")

st.subheader("💡 Motivation for Today")    
st.write(random.choice(quotes))

st.write("---")
st.write("Made with ❤️ using Streamlit")
