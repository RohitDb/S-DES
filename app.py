import streamlit as st
import pickle 
import pandas as pd 
import numpy as np  
from PIL import Image 


def main():
 st.title("Bank Application")
 st.write("Please feel free to enter rhe data")
 st.write("[Data is end to end encrypted >](https://google.com)")
 html_temp = """
    <div style="background-color:tomato;padding:10px;margin:20px   .radio-placeholder > .stRadio > label > span {
        color: #999999;
    }">
    <h2 style="color:white;text-align:center;">Bank application </h2>
    </div>
    
    """
 st.markdown(html_temp,unsafe_allow_html=True)
 st.subheader("Enter the data:")
 name=st.text_input("Name","Type here")

 if st.button("Preduct"):
   
    st.success("Bank balance")   
    st.subheader("10000000")
    
if __name__ == "__main__": 
 main()

