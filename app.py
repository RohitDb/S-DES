import streamlit as st
import pickle 
import pandas as pd 
import numpy as np  
from PIL import Image 
from client import client


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
 username=st.text_input("Enter Username")
 account=st.text_input("Enter account_no")


 if st.button("Get bank balance"):
    amount=client(username,account)
    st.success("Bank balance")   
    st.subheader(amount)
    
if __name__ == "__main__": 
 main()
