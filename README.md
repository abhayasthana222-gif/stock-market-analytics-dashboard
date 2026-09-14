#  STOX iQ — Stock Market Analytics Dashboard

An end-to-end stock market analytics project combining **Python** for live data collection and analysis, and **Power BI** for interactive dashboard visualization.

##  Overview

This project fetches live stock market data for 25+ global companies, cleans and processes it using Python, computes key financial metrics, and visualizes everything in an interactive Power BI dashboard designed for investors and analysts to track performance at a glance.

##  Tech Stack

- **Python** — pandas, yfinance, openpyxl
- **Power BI** — Data modeling, DAX measures, interactive visuals
- **DAX** — Custom measures for returns, volatility, and moving averages

##  Features

- **Live data pipeline**: Fetches real-time stock data via the yfinance API
- **Data cleaning & processing**: Handles missing values, formats dates, standardizes columns
- **Calculated metrics**: Daily returns, 7-day & 30-day moving averages, volatility, period return
- **Interactive KPI cards**: Latest Close, Total Volume, Avg Daily Return %, Period Return %, Volatility, Max/Min Closing Price
- **Visualizations**:
  - Price trend line chart across 25+ stocks
  - Gain/loss bar chart with conditional color formatting (green/red)
  - Portfolio value treemap by stock
  - Sector-wise exposure pie chart
- **Cross-filtering & slicers**: Filter the entire dashboard by stock symbol or sector
- **Multi-page report** with page navigation

##  Screenshots
<img width="918" height="586" alt="image" src="https://github.com/user-attachments/assets/86630950-4a9e-42b1-b9d9-41a96d15475b" />
<img width="928" height="520" alt="image" src="https://github.com/user-attachments/assets/1c7713fa-2d87-42de-84fb-6e20e19077f3" />
##  Project Structure

├── dash.py                     # Python script to fetch, clean & analyze stock data
├── stock_dashboard.pbix        # Power BI dashboard file
├── dashboard_page1.png         # Dashboard preview
├── dashboard_page2.png         # Dashboard preview
└── README.md

##  How to Run

1. Install dependencies:
   pip install yfinance pandas openpyxl

2. Run the data pipeline:
   python dash.py

   This generates stock_dashboard_data.xlsx with cleaned, analyzed stock data.

3. Open stock_dashboard.pbix in Power BI Desktop — it's connected to the generated Excel file.

##  Key DAX Measure Example

Period Return % =
VAR varFirstDate = MIN('Raw Data'[Date])
VAR varLastDate = MAX('Raw Data'[Date])
VAR varFirstClose = CALCULATE(AVERAGE('Raw Data'[Closing Price]), 'Raw Data'[Date] = varFirstDate)
VAR varLastClose = CALCULATE(AVERAGE('Raw Data'[Closing Price]), 'Raw Data'[Date] = varLastDate)
RETURN DIVIDE(varLastClose - varFirstClose, varFirstClose) * 100

##  About Me

Built by **Abhay Asthana** — Data Analyst based in Delhi, skilled in Python, SQL, Power BI, and data visualization.

[LinkedIn](https://www.linkedin.com/in/abhay-asthana-691505395)
