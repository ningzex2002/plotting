# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:38:37 2021

@author: ningz
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Plotting Tool")

st.markdown("[Ningze Xia](https://github.com/ningzex2002)")

uploaded_file = st.file_uploader(label = "Choose a file to upload",type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = df.applymap(lambda x: np.nan if x == " " else x)
    
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
        
    good_cols = [c for c in df.columns if can_be_numeric(c)]
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis=0)
    
    x_axis = st.selectbox("Choose an x value", good_cols)
    y_axis = st.selectbox("Choose a y value", good_cols)
    colors = st.selectbox("Choose a column for color", good_cols)
    
    max = len(df.iloc[:, [0]])
    slider = st.slider("Select a range of rows",0,max-1,(0,max-1))

    
    st.write(f"The user chose {y_axis} as y axis and {x_axis} as x axis for rows {slider}")
    
    
    graph = alt.Chart(df.iloc[slider[0]:slider[1],:]).mark_circle().encode(
        x= x_axis, 
        y= y_axis, 
        color = alt.Color(colors,scale = alt.Scale(scheme = "dark2"))
    )
    
    st.altair_chart(graph)
    
    
    