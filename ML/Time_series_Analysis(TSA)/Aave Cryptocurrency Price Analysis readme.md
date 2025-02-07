Aave Cryptocurrency Price Analysis & Forecasting

🔍 Overview
This script analyzes and predicts the daily closing prices of Aave cryptocurrency using time series analysis techniques. It helps identify trends, seasonality, and patterns in historical price data while forecasting future prices using ARIMA models.

⚡ How It Works
Loads and processes the dataset

Uploads the Aave price dataset (CSV file).
Parses the 'Date' column and sets it as an index for time series analysis.
Performs Trend and Seasonality Analysis

Uses Seasonal Decomposition to separate the data into trend, seasonality, and residual components.
Visualizes these components to understand price movement patterns.
Applies Fourier Transform for Frequency Analysis

Identifies periodic cycles in the data.
Plots a Power Spectrum to visualize dominant frequencies affecting price movement.
Checks Stationarity using the Augmented Dickey-Fuller (ADF) Test

Determines if the time series is stationary (required for forecasting models).
If the data is non-stationary, suggests transformations to stabilize it.
Builds an ARIMA Model for Forecasting

Uses an AutoRegressive (AR) model to predict future prices.
Fits the model to historical data and generates a 365-day forecast (1-year prediction).
Visualizes the Forecast

Plots actual vs. predicted prices.
Displays confidence intervals to indicate prediction reliability.

🔧 Requirements
Ensure you have the following Python libraries installed before running the script:
pip install pandas numpy statsmodels matplotlib

🚀 How to Run
Upload the dataset (Aave.csv) when prompted.
Run the script in Python or Google Colab:
python script_name.py
The script will analyze the historical data and generate a forecast plot showing predicted prices.
📌 Features
✅ Loads and processes Aave historical price data
✅ Performs trend, seasonality, and residual analysis
✅ Uses Fourier Transform for frequency analysis
✅ Checks for stationarity with the ADF test
✅ Builds an ARIMA model for price forecasting
✅ Generates a 1-year forecast with confidence intervals

📂 Expected Outputs
Trend & Seasonality Decomposition → Helps understand price movement over time.
Power Spectrum Analysis → Shows dominant price movement frequencies.
Stationarity Test Result → Confirms if the dataset is stable for forecasting.
ARIMA Model Summary → Displays model parameters & accuracy.
Forecasted Prices Plot → Visual representation of price predictions for the next 365 days.
📊 Sample Forecast Output
📌 Red Line: Predicted Prices
📌 Pink Shaded Area: Confidence Intervals (Indicates how reliable the forecast is)


🛑 How to Stop Execution
If you need to stop the script while running, press:
CTRL + C