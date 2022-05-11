import streamlit as st
import pandas as pd 
import plotly.express as px

#writing the function. 
#Turning csv file into dataframe

@st.cache
def load_data():
    """ Function for loading data"""
    df =pd.read_csv("data/airbnb_listings_2021.csv", index_col = "id")
    
    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns
    
    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns
    
    
    return df, numeric_cols, text_cols


df, numeric_cols, text_cols = load_data()

#Title for the dashboard

st.title(" Airbnb Dashboard")

# showing dataset 
st.write(df)

#Adding checkbox to sidebar

check_box = st.sidebar.checkbox(label = "Display dataset")

if check_box:
    #show the dataset
    st.write(df)
    
#giving sidebar a title

st.sidebar.title("Settings")
feature_selection =st.sidebar.multiselect(label = "Variables" , options =numeric_cols)

print(feature_selection)
df_features = df[feature_selection]
plotly_figure = px.line(data_frame=df_features, x=df_features.index, y=feature_selection)