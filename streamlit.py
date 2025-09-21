# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 16:16:26 2025

@author: manee
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
def welcome():
    return "welcome"

def predict_note(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if prediction>0.5:
        result="Its  not Bank note"
    else:
        result="Its Bank note"
        
    return result


def main():
    st.title("Bank Authenticator")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance"," ")
    skewness = st.text_input("skewness"," ")
    curtosis = st.text_input("curtosis"," ")
    entropy = st.text_input("entropy"," ")
    result=""
    if st.button("Predict"):
        result=predict_note(variance,skewness,curtosis,entropy)
    st.success(' {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main()