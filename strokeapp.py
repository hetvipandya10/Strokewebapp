import streamlit as st

st.title("Welcome to stroke App")

gender=st.slider("Select gender=",0,2)
age=st.slider("Select age=",0,82)
hypertension=st.slider("Select hypertension=",0,1)
heart_disease=st.slider("Select heart_diseases=",0,1)
ever_married=st.slider("Select ever_married=",0,1)
work_type=st.slider("Select work_type=",0,4)
Residence_type=st.slider("Select Residence_type=",0,1)
avg_glucose_level=st.slider("Select avg_glucose_level=",55,27)
bmi=st.slider("Select bmi=",10,97)
smoking_status=st.slider("Select smoking_status=",0,3)

import pickle
model=pickle.load(open("stroke.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
    st.success("The stroke is "+ str(prd[0]))

