import streamlit as st
import pickle 
import pandas as pd 
import numpy as np  
from PIL import Image 


def main():
 st.title("Depression Analyser")
 st.write("Please feel free to enter rhe data")
 st.write("[Data is end to end encrypted >](https://google.com)")
 html_temp = """
    <div style="background-color:tomato;padding:10px;margin:20px   .radio-placeholder > .stRadio > label > span {
        color: #999999;
    }">
    <h2 style="color:white;text-align:center;">Depression Analyser </h2>
    </div>
    
    """
 st.markdown(html_temp,unsafe_allow_html=True)
 st.subheader("Enter the data:")
 name=st.text_input("Name","Type here")

 if st.button("Preduct"):
   
    st.success("Depression level:")   
    st.subheader(result)
    
if __name__ == "__main__": 
 main()

