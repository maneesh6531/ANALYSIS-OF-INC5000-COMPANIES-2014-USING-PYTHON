📊 Inc5000 Company Analysis (2014) – Python Data Analysis Project

This project analyzes the Inc5000 fastest-growing U.S. companies (2014) using Python.
It focuses on growth trends, revenue patterns, industry distributions, geographic insights, and company-size behavior using real-world business data.

📁 Project Files
File	Description
project.py	Full Python code for analysis, preprocessing, and visualizations
Data Set- Inc5000 Company List_2014.csv	Dataset used for the analysis
python report.docx	Complete project documentation
📌 Dataset Information

Source: Tableau Public Sample Data

Link: https://public.tableau.com/app/learn/sample-data

Entries: ~5000 companies

Key Features:

company

growth (3-year growth rate)

revenue (USD)

workers

industry

state_s

yrs_on_list

🛠️ Tools & Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

🧹 Data Preprocessing Steps

Removed blank and irrelevant columns

Handled missing values using median replacement

Converted growth and revenue to numeric formats

Filtered valid U.S. companies

Created derived fields:

Growth categories

Company size (Small/Medium/Large)

📈 Key Analysis Performed
1️⃣ Industry Trends

Top industries by company count

Industries with highest average growth rates

2️⃣ Geographic Distribution

Top U.S. states with most companies

Highest-growth states (average growth comparison)

3️⃣ Growth vs Revenue

Scatter plot with log-scale revenue

Weak positive correlation between growth and revenue

4️⃣ Company Size Impact

Smaller companies (<100 workers) grow faster on average

Larger companies generate higher revenue

5️⃣ Years on List

Repeat companies have higher revenue than first-timers

Growth distribution compared across years on list

6️⃣ Top Companies

Top 10 by growth rate

Top 10 by revenue

📊 Visualizations Included

Bar charts (industries, states)

Scatter plots (growth vs revenue)

Distribution plots (company size)

Box plots (years on list)

Pair plots (growth, revenue, workers, yrs_on_list)

Correlation heatmap

🧠 Insights & Findings

Health and IT sectors dominate the list

Growth does not strongly correlate with revenue

California, Texas, and New York host the most companies

Small companies show higher growth rates

Repeat companies tend to earn more revenue

🚀 Future Enhancements

Apply machine learning models for growth prediction

Use GeoPandas for interactive geographic mapping

Compare Inc5000 trends across multiple years (2010–2024)

Deploy dashboard using Plotly or Streamlit

🙌 Acknowledgements

Dataset by Inc. Magazine & Tableau Public

Project completed under LPU, INT375 – Data Science Toolbox: Python Programming
