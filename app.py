import streamlit as st
import pandas as pd
import numpy as np
import pickle

model=pickle.load(open('model.pkl', 'rb'))
encoder=pickle.load(open('target_encoder.pkl', 'rb'))
transformer=pickle.load(open('transformer.pkl', 'rb'))

st.title("Medical Insurance Premium Prediction")

sex=st.selectbox("Please select your gender",('Male','Female'))

age=st.text_input("Enter your age",28)

bmi=st.text_input("Enter your BMI",20)
bmi=float(bmi)

children=st.selectbox("Please select the number of children",(0,1,2,3,4,5,6,7,8,9,10))
children=int(children)

smoker=st.selectbox("Please select your smoking status",('Yes','No'))

region=st.selectbox("Please select your region",
                    ('southeast','southwest','northeast','northwest'))

# Storing everything in a dictionary
l={}
l['age']=age
l['sex']=sex
l['bmi']=bmi
l['children']=children
l['smoker']=smoker
l['region']=region

df=pd.DataFrame(l,index=[0])

# Encode all the categorical columns

df['region']=encoder.transform(df['region'])
df['smoker']=df['smoker'].map({'Yes':1,'No':0})
df['sex']=df['sex'].map({'Male':1,'Female':0})

df=transformer.transform(df)
y_pred=model.predict(df)

if st.button("Submit and show results"):
    st.header(f"{round(y_pred[0],2)} INR")