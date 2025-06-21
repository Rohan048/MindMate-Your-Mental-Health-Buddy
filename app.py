import streamlit as st
import pandas as pd
from datetime import datetime
from utils import save_mood, load_data, mood_chart
from activities import get_suggestion

st.set_page_config(page_title="MindMate", page_icon="🧠")
st.title("🧠MindMate-Your Mental Health Buddy")

# Mood Check-in
st.subheader("📅 How are you feeling today?")
mood = st.radio("Select your mood", ['Choose' , 'Happy', 'Sad', 'Angry', 'Anxious', 'Calm' , 'Alone'])
note = st.text_area("Write about your thoughts (optional)")

if st.button("Save Mood"):
    save_mood(mood, note)
    st.success("Mood saved successfully!")

# Mood Graph
st.subheader("📊 Your Mood Trends")
data = load_data()
if not data.empty:
    mood_chart(data)
else:
    st.info("No mood data yet.")

# Suggestions
st.subheader("💡 Self-Care Suggestion")
suggestion = get_suggestion(mood)
st.write(suggestion)

# Gif & Music depend on Mood
if mood in ['Choose']:
    ""
elif mood in ['Anxious']:
    st.image("assets/breathing.gif", caption="Follow this breathing exercise", use_container_width=True)
    st.audio("assets/breathing.mp3")

elif mood in ['Happy']:
    st.image("assets/happy.gif", caption="Enjoy The Day😂👍 ", use_container_width=True)
    st.audio("assets/happy.mp3")

elif mood in ['Sad']:
    st.image("assets/sad.gif", caption="Go For a Short Walk🚶❤️ ", use_container_width=True)
    st.audio("assets/sad.m4a")

elif mood in ['Angry']:
    st.image("assets/angry.gif", caption="Take a Deep Breath😤☺️ ", use_container_width=True)
    st.audio("assets/angry.mp3")

elif mood in ['Calm']:
    st.image("assets/calm.gif", caption="Go for Long Drive❤️ ", use_container_width=True)
    st.audio("assets/calm.mp3")

elif mood in ['Alone']:
    st.image("assets/alone.gif", caption="Watch Favourite Movies & Series👌 ", use_container_width=True)
    st.audio("assets/alone_music.m4a")
    st.write("You can watch this funny Movie😂")

st.markdown("""
    <div style='text-align: center;'>
        <small>Made with ❤️ by <b>Rohan Rai</b></small><br>
        <a href='https://github.com/rohan048' target='_blank'>GitHub</a> | 
        <a href='https://www.linkedin.com/in/rohan-kumar-rai-8a711126b/' target='_blank'>LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)
