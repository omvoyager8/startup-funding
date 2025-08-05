# 📊 Startup Funding Analysis Dashboard

An interactive dashboard built with **Streamlit** to explore startup funding trends in India. It helps users understand how much funding startups raised, where they are located, and who invested in them — using **overall metrics, startup-wise views, and investor-focused analysis**.

---

## 📁 Project 1: Data Cleaning 

### 🚀 Overview:
Cleaned raw startup funding data to prepare it for analysis and visualization. This includes handling missing values, standardizing formats, renaming columns, and feature extraction.

### 🛠 Tools & Techniques:
- **Jupyter Notebook**
- **Pandas** for data manipulation
- **Datetime handling** for date conversion and feature engineering

### 🔍 Key Steps:
- Converted date column to datetime format
- Extracted year and month from date
- Cleaned and standardized startup names and investor entries

---

## 📁 Project 2: Streamlit Dashboard App

### 🚀 Overview:
A web-based dashboard to analyze startup funding patterns using `Streamlit`. It includes interactive visualizations and detailed filtering by startup or investor.

### 🛠 Tools & Techniques:
- Streamlit for building UI
- Pandas for data manipulation
- Matplotlib, Seaborn, Plotly for charts

### 📈 Dashboard Features:
- Overall metrics: Total funding, Max/Avg funding, Number of startups
- MOM trend line charts
- Individual startup profile with city, verticals, and funding rounds
- Investor insights with investment history and distribution by sector, round, and city

---

## 📁 Project 3: Dataset

### 📄 Startup_cleaned2.csv
A cleaned dataset containing:
- Startup names
- Cities
- Sectors (verticals and subverticals)
- Amounts funded
- Date of funding
- Round and investor names

---

## 📁 Project 4: Requirements

### 📄 requirements.txt
Contains all necessary packages to run the Streamlit app:

- streamlit==1.47.1  
- pandas==2.3.1  
- matplotlib==3.9.0  
- seaborn==0.13.2  
- plotly==5.22.0  

Install them using:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the App

1. Clone the repo:
```bash
git clone https://github.com/your-username/startup-funding-analysis.git
cd startup-funding-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 🤝 Developed by Om Gonjari

- [LinkedIn](https://www.linkedin.com/in/omgonjari/)
- [GitHub](https://github.com/omvoyager8/)
