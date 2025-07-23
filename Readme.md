# 📊 Customer Churn Analysis – EDA, Prediction, and Dashboard

This project explores the **Telco Customer Churn** dataset through Exploratory Data Analysis (EDA), builds a basic predictive model using **logistic regression**, and presents insights through an interactive **Streamlit dashboard**.

It is a full-stack data analysis project suitable for portfolios and resumes.

---

## 🔍 Project Features

- ✅ Performed univariate, bivariate, and multivariate EDA using Pandas, Seaborn, and Matplotlib
- ✅ Identified key churn drivers such as tenure, contract type, and monthly charges
- ✅ Handled missing data, type conversions, and encoding
- ✅ Built a logistic regression model (~80% accuracy)
- ✅ Deployed a simple interactive dashboard using Streamlit
- 📎Live Dashboard:https://abinash9012-customer-churn-eda-appstreamlit-app-rdpc89.streamlit.app/

---

## 📁 Project Structure
customer-churn-eda/
├── data/
│ └── telco_churn.csv
├── notebooks/
│ └── eda_churn_analysis.ipynb
├── app/
│ └── streamlit_app.py
├── images/
│ └── *.png (all saved plots)
├── requirements.txt
└── README.md

---

## 💻 Tech Stack

- **Languages**: Python
- **Libraries**: Pandas, NumPy, Seaborn, Matplotlib, scikit-learn, Streamlit
- **Tools**: Jupyter Notebook, Git, GitHub, Streamlit Cloud

---

## 📊 Key EDA Insights

- Customers with **month-to-month contracts** churn at a much higher rate.
- Lower tenure and **higher monthly charges** are strong churn predictors.
- Fiber optic internet users churn more than DSL users.

---

## 🔮 Model Overview

- **Model**: Logistic Regression
- **Target**: `Churn` (Yes/No)
- **Accuracy**: ~80%
- **Preprocessing**: One-hot encoding, type conversion, missing value imputation

---

## 🌐 Live Streamlit Dashboard (Optional)

> To deploy your dashboard online:
1. Push this project to GitHub
2. Sign into [Streamlit Cloud](https://streamlit.io/cloud)
3. Select your repo and set `app/streamlit_app.py` as the entry point
4. Done! You’ll get a public URL to share

---

## ▶️ Local Setup Instructions

```bash
# 1. Clone this repo
git clone https://github.com/yourusername/customer-churn-eda.git
cd customer-churn-eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Jupyter Notebook (for EDA)
jupyter notebook notebooks/eda_churn_analysis.ipynb

# 4. Run the Streamlit dashboard (optional)
streamlit run app/streamlit_app.py

