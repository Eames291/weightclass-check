import streamlit as st
import joblib
joblib.dump(clf,'model_new')
model = joblib.load('model_new')
st.title("Non-Combative Weight Class Calculator")
weight = st.slider('What is your weight?', 0, 100)
height = st.slider('What is your height?', 0, 200)
result = model.predict([[weight,height]])
if st.button("Calculate"):
  st.write(f"You are {result}")

