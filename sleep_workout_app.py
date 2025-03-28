import streamlit as st
from datetime import time
import joblib

# --- Load ML model ---
model = joblib.load("workout_model.pkl")

def predict_workout_model(sleep, quality, deep):
    return model.predict([[sleep, quality, deep]])[0]

# --- Duration and Calories ---
duration_map = {
    "Rest": 0,
    "Stretching": 15,
    "Light Cardio": 20,
    "Cardio": 30,
    "Strength": 30,
    "HIIT": 25
}

calories_map = {
    "Rest": 0,
    "Stretching": 60,
    "Light Cardio": 120,
    "Cardio": 250,
    "Strength": 220,
    "HIIT": 300
}

# --- Streamlit UI ---
st.set_page_config(page_title="Sleep-Based Workout", layout="centered")
st.title("😴 Sleep-Based Workout Recommendation")
st.markdown("Enter your sleep data to get a workout recommendation.")

# Input form
date = st.date_input("Date", help="Enter the date of your sleep record")
sleep = st.number_input("Sleep Hours", min_value=0, max_value=24, step=1, format="%d", help="Total hours slept")
quality = st.slider("Sleep Quality (%)", 0, 100, 0, help="Estimate of overall sleep quality")
deep = st.slider("Deep Sleep (%)", 0, 100, 0, help="Estimate of deep sleep portion")
wake = st.time_input("Wake-Up Time", value=time(0, 0), help="When you woke up")

# Button
if st.button("Get Recommendation"):
    if sleep == 0 and quality == 0:
        st.warning("Please enter valid sleep data.")
    else:
        workout = predict_workout_model(sleep, quality, deep)
        duration = duration_map.get(workout, 0)
        calories = calories_map.get(workout, 0)

        st.subheader("🏋️ Recommendation")
        st.write(f"**Workout Type:** {workout}")
        st.write(f"**Duration:** {duration} mins")
        st.write(f"**Estimated Calories Burned:** {calories}")
