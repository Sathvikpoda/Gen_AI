Job Postings Analysis Tool

This repository contains a Python script designed to analyze job postings data from a CSV file. The script provides insights into the distribution of job roles and the frequency of job postings over time. It utilizes Pandas for data manipulation, Matplotlib for visualization, and regular expressions for date parsing.

Description
The script performs two main analyses:

Job Roles Analysis: It categorizes job titles into predefined roles such as Frontend Developer, Backend Developer, etc., and visualizes the distribution of these roles among the job postings.
Daily Postings Analysis: It converts relative dates (e.g., 'Posted 3 days ago') into actual dates and displays the number of job postings per day.
Key Features
Data Visualization: Generates pie charts and bar graphs to visually represent the data.
Date Conversion: Transforms relative date strings into absolute dates using regex and datetime operations.
Error Handling: Checks for missing columns and unparsed dates, ensuring robust data handling.
Technologies Used
pandas: For data reading and manipulation.
matplotlib: For creating visualizations.
datetime: For handling date transformations.
re: For parsing and converting relative date strings.

How to Run
To run this script:

Ensure you have Python installed along with the necessary libraries (pandas, matplotlib).
Update the csv_filename path in the script to point to your CSV file containing job postings data.

Run the script from your terminal or command prompt:
python job_postings_analysis.py
Setup

Before running the script, install all required Python packages using pip:
pip install pandas matplotlib
Results
Upon execution, the script will:

Display a pie chart showing the percentage distribution of job roles.
Show a bar graph indicating the number of job postings for each date.