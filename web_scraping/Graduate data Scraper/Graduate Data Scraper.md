Graduate Data Scraper

This repository contains a Python script that automates the process of scraping graduate data from a specific website using Selenium. The script navigates through web forms, submits queries based on application IDs, and extracts structured data, saving it into a CSV file.

Description
The script uses Selenium WebDriver to interact with a web form, inputting a series of graduate application IDs and extracting the corresponding data displayed on the webpage. It is designed to handle multiple IDs sequentially and capture the associated data for each ID.

Key Features
Automated Form Interaction: Automates inputting data into web forms and clicking buttons.
Data Extraction: Captures specific data points from the resulting webpage after form submission.
Sequential Processing: Handles a series of application IDs, processing each in turn.
Data Storage: Outputs the collected data into a CSV file for easy analysis and storage.
Technologies Used
selenium: For automating web browser interaction.
pandas: For organizing extracted data into a structured format and saving it to CSV.
webdriver_manager: For managing the browser driver automatically.
How to Run
To run this script:

Ensure you have Python installed along with the necessary libraries (selenium, pandas, and webdriver_manager).
Download or clone this repository to your local machine.
Ensure that you have the correct path to your ChromeDriver and that it is updated.
Adjust the start_app_id and end_app_id in the script to the range of IDs you want to scrape.

Run the script from your terminal or command prompt:
python scrapinrg.py
Setup

Before running the script, make sure to install all required Python packages using pip:
pip install selenium pandas webdriver_manager

Results
Upon execution, the script will:

Navigate to the specified webpage.
Automatically input and submit the application IDs in the specified range.
Extract the data for each ID and compile it into a DataFrame.
Save the DataFrame to a CSV file named f18_graduate_data_range.csv.
Print a message indicating the completion of data scraping and the location of the saved CSV file.
