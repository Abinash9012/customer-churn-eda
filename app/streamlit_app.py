import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/telco_churn.csv")

# Title
st.title("📊 Telco Customer Churn Analysis")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Churn count
st.subheader("Churn Distribution")
fig, ax = plt.subplots()
sns.countplot(x='Churn', data=df, ax=ax)
st.pyplot(fig)

# Monthly Charges Distribution
st.subheader("Monthly Charges vs Churn")
fig2, ax2 = plt.subplots()
sns.boxplot(x='Churn', y='MonthlyCharges', data=df, ax=ax2)
st.pyplot(fig2)

# Sidebar filter
contract = st.sidebar.selectbox("Filter by Contract Type", df["Contract"].unique())
filtered = df[df["Contract"] == contract]
st.subheader(f"Filtered View – {contract} Contracts")
st.write(filtered[['Churn', 'MonthlyCharges', 'tenure']].head())
