# 📊 Candlestick Chart Visualization Using Python

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue.svg">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg">
<img src="https://img.shields.io/badge/Matplotlib-Visualization-orange.svg">
<img src="https://img.shields.io/badge/Stock%20Market-Candlestick%20Charts-red.svg">
<img src="https://img.shields.io/badge/Status-Completed-success.svg">
</p>

---

# 📖 Overview

This project was completed as part of the **Python Developer Internship at Hackveda Solutions**.

The objective of this task was to read historical stock market data from a CSV file, preprocess the data, and visualize stock price movements using **Candlestick Charts**.

Candlestick charts are among the most widely used visualization techniques in financial markets. They provide traders and analysts with valuable insights into market behavior by displaying the opening, closing, highest, and lowest prices of a stock during a specific time period.

This project demonstrates how Python can be used for financial data processing and visualization to better understand market trends.

---

# 🎯 Project Objective

The objectives of this task were to:

* Read stock market data from a CSV dataset.
* Load and process the dataset using Pandas.
* Clean and preprocess financial data.
* Understand Open, High, Low, and Close (OHLC) values.
* Generate candlestick charts using Python.
* Visualize historical stock price movements.
* Learn the fundamentals of financial data visualization.

---

# 📚 Project Description

Financial institutions and traders often use candlestick charts to analyze market trends and make informed investment decisions.

In this project, historical stock market data for **BANKBARODA** was provided in CSV format.

The workflow involved:

* Importing the dataset.
* Cleaning and validating the data.
* Preparing the dataset for visualization.
* Plotting candlestick charts.
* Understanding price movements through graphical analysis.

This project serves as a practical introduction to financial data analytics using Python.

---

# 📈 What is a Candlestick Chart?

A candlestick chart is a graphical representation of a stock's price movement over a selected time interval.

Each candlestick displays four important price values:

* **Open Price** – The price at which trading started.
* **High Price** – The highest price reached during the trading session.
* **Low Price** – The lowest price reached during the trading session.
* **Close Price** – The final trading price at market close.

By combining these values, candlestick charts help traders identify trends, reversals, and market sentiment.

---

# 🟢 Bullish Candlestick

A bullish candlestick indicates that the stock closed at a higher price than it opened.

This generally represents buying pressure and positive market sentiment.

---

# 🔴 Bearish Candlestick

A bearish candlestick indicates that the stock closed at a lower price than it opened.

This generally represents selling pressure and negative market sentiment.

---

# ✨ Features

* Read CSV stock market dataset
* Load data using Pandas
* Data cleaning and preprocessing
* Handle missing values
* Convert data into appropriate formats
* Generate candlestick charts
* Visualize stock price movement
* Analyze market trends
* Easy-to-understand financial visualization

---

# 🛠 Technologies Used

## Programming Language

* Python 3

## Libraries

* Pandas
* Matplotlib
* mplfinance (or Plotly, depending on implementation)
* NumPy

## Tools

* Visual Studio Code
* Git
* GitHub

---

# 📂 Project Structure

```text
Task - 3 Candlestick Chart Visualization/

│── data/
│     └── StockDataBANKBARODA.csv
│
├── candlestick_chart.py
├── requirements.txt
├── README.md
└── presentation/
```

---

# ⚙ Prerequisites

Before running the project, ensure the following are installed:

* Python 3.9 or above
* pip package manager

Install the required libraries:

```bash
pip install pandas matplotlib mplfinance
```

or

```bash
pip install -r requirements.txt
```

---

# ▶ How to Run

### Step 1

Clone the repository.

```bash
git clone https://github.com/mohammedzubairuddinzameer/Hackveda-Internship-projects-tasks.git
```

---

### Step 2

Navigate to the project folder.

```bash
cd "Task - 3 Candlestick Chart Visualization"
```

---

### Step 3

Install dependencies.

```bash
pip install -r requirements.txt
```

---

### Step 4

Run the Python script.

```bash
python candlestick_chart.py
```

---

# 🔄 Project Workflow

```text
Historical CSV Dataset
          │
          ▼
Read Dataset using Pandas
          │
          ▼
Data Cleaning
          │
          ▼
Preprocessing
          │
          ▼
Prepare OHLC Data
          │
          ▼
Generate Candlestick Chart
          │
          ▼
Visualize Stock Trends
```

---

# 📊 Dataset Information

The dataset contains historical trading information for **BANKBARODA** stock.

Typical columns include:

* Date
* Open Price
* High Price
* Low Price
* Close Price
* Adjusted Close
* Volume

These values are essential for generating candlestick charts.

---

# 📉 Data Preprocessing

Before visualization, the following preprocessing steps were performed:

* Reading CSV file
* Removing missing values
* Converting Date column into datetime format
* Sorting data chronologically
* Setting the Date column as the index
* Validating OHLC values

Proper preprocessing ensures accurate chart generation.

---

# 📊 Expected Output

After successful execution, the program displays:

* Historical BANKBARODA stock prices
* Candlestick chart visualization
* Market trend representation
* Daily price movements
* Interactive or static financial chart (depending on implementation)

---

# 🌍 Real-World Applications

Candlestick charts are widely used in:

* Stock Trading
* Investment Analysis
* Financial Institutions
* Brokerage Platforms
* Algorithmic Trading
* Portfolio Management
* Cryptocurrency Analysis
* Forex Trading
* Commodity Markets

Popular trading platforms such as TradingView, Zerodha Kite, Groww, and Investing.com use candlestick charts extensively.

---

# 🎓 Learning Outcomes

Through this project, I learned:

* Financial data analysis
* CSV file handling
* Data preprocessing
* Pandas DataFrames
* Data visualization
* Candlestick chart construction
* OHLC data analysis
* Python libraries for financial analysis
* Market trend interpretation
* Basic technical analysis

---

# 💡 Challenges Faced

During this task, several practical challenges were encountered:

* Understanding OHLC data structure
* Formatting financial datasets correctly
* Handling missing and inconsistent values
* Learning financial visualization libraries
* Choosing appropriate chart settings
* Interpreting candlestick patterns

Overcoming these challenges improved both programming and analytical skills.

---

# 🚀 Future Improvements

Possible future enhancements include:

* Interactive candlestick charts using Plotly
* Live stock market data integration
* Multiple stock comparison
* Technical indicator overlays (RSI, MACD, SMA)
* Trend prediction using Machine Learning
* Export charts as images or PDF
* Streamlit dashboard
* User-selectable date ranges

---

# 📚 Key Skills Acquired

✔ Python Programming

✔ Pandas

✔ Data Cleaning

✔ Financial Data Analysis

✔ CSV Processing

✔ Matplotlib

✔ Data Visualization

✔ Candlestick Charts

✔ Technical Analysis Basics

✔ Problem Solving

---

# 🙏 Acknowledgements

This project was completed during the **Python Developer Internship at Hackveda Solutions**.

The task provided valuable practical exposure to financial data processing, stock market visualization, and Python-based data analytics.

---

# 👨‍💻 Author

**Mohammed Zubair Uddin**

Python Developer | Data Science Student

**GitHub:**
https://github.com/mohammedzubairuddinzameer

**LinkedIn:**
https://www.linkedin.com/in/mohammed-zubair-uddin-zameer

---

# 📄 License

This project is intended for educational purposes and was completed as part of the Hackveda Python Developer Internship.

It is shared for learning, reference, and academic use.
