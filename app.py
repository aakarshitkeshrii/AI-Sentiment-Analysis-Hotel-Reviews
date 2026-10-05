
import streamlit as st
import pandas as pd

df = pd.read_csv("sentiment_results.csv")

st.title("Hotel Review Sentiment Dashboard")

total_reviews = len(df)

positive_reviews = len(
    df[df["Sentiment"]=="Positive"]
)

negative_reviews = len(
    df[df["Sentiment"]=="Negative"]
)

neutral_reviews = len(
    df[df["Sentiment"]=="Neutral"]
)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total", total_reviews)
col2.metric("Positive", positive_reviews)
col3.metric("Negative", negative_reviews)
col4.metric("Neutral", neutral_reviews)

st.bar_chart(
    df["Sentiment"].value_counts()
)

option = st.selectbox(
    "Filter Sentiment",
    ["All","Positive","Negative","Neutral"]
)

if option != "All":
    filtered_df = df[df["Sentiment"] == option]
else:
    filtered_df = df

st.write(filtered_df.head(50))
