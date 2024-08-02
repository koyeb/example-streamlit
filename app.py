import streamlit as st
import time


st.title("Streamlit, Deployed on Koyeb")
st.subheader("Let's celebrate!")

progress_text = "Inflating the balloons..."
my_progress = st.progress(0, text=progress_text)

for percent in range(100):
    time.sleep(0.05)
    my_progress.progress(percent + 1, text=progress_text)

my_progress.empty()
st.balloons()
st.button("Re-run")
