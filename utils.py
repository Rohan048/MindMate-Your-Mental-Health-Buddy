import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import streamlit as st

def save_mood(mood, note):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([[time, mood, note]], columns=['Timestamp', 'Mood', 'Note'])
    df.to_csv('mood_data.csv', mode='a', header=not pd.io.common.file_exists('mood_data.csv'), index=False)

def load_data():
    try:
        return pd.read_csv('mood_data.csv')
    except:
        return pd.DataFrame(columns=['Timestamp', 'Mood', 'Note'])

def mood_chart(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    mood_counts = df.groupby(df['Timestamp'].dt.date)['Mood'].value_counts().unstack().fillna(0)
    st.line_chart(mood_counts)
