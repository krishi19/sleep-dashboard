import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
df.columns = df.columns.str.replace(" ", "_")

st.title("🛌 Sleep Health & Lifestyle Dashboard")

# Sidebar filters
gender = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())
disorder = st.sidebar.multiselect("Select Sleep Disorder", df["Sleep_Disorder"].unique(), default=df["Sleep_Disorder"].unique())

filtered = df[df["Gender"].isin(gender) & df["Sleep_Disorder"].isin(disorder)]

# Summary
st.subheader("📊 Summary Statistics")
st.write(filtered.describe())

# Boxplot: Sleep Duration by Occupation
st.subheader("🧠 Sleep Duration by Occupation")
fig1 = px.box(filtered, x="Occupation", y="Sleep_Duration", color="Gender")
st.plotly_chart(fig1)

# Scatter: Steps vs Sleep
st.subheader("💤 Sleep Duration vs Daily Steps")
fig2 = px.scatter(filtered, x="Daily_Steps", y="Sleep_Duration", size="Stress_Level",
                  color="Sleep_Disorder", hover_data=["Occupation", "Age"])
st.plotly_chart(fig2)

# Animated Scatter
st.subheader("🎞️ Animated: Steps vs Sleep Across Age")
fig3 = px.scatter(filtered, x="Daily_Steps", y="Sleep_Duration", animation_frame="Age",
                  color="Sleep_Disorder", size="Stress_Level", hover_data=["Gender", "Occupation"])
st.plotly_chart(fig3)
