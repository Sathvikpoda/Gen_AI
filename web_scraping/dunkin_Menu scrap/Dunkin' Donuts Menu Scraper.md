Dunkin' Donuts Menu Scraper and Viewer

This repository contains Python scripts designed to interact with the Dunkin' Donuts menu webpage. The scripts perform tasks such as scraping menu items and their descriptions, saving the HTML content locally, and opening the Dunkin' Donuts menu in a Chrome browser.

Description
The scripts in this repository serve three main functions:

Scrape Dunkin' Donuts Menu: Extracts menu items and their descriptions from the Dunkin' Donuts menu page and saves them as a CSV file.
Save and View HTML Locally: Downloads the HTML content of the Dunkin' Donuts menu page, saves it locally, and opens it in a Chrome browser.
Open Menu URL in Chrome: Directly opens the Dunkin' Donuts menu page in a Chrome browser using Selenium.

Key Features
Menu Scraping: Automates the extraction of menu items, categorizing them by section and detailing item descriptions.
HTML Content Handling: Downloads and saves the webpage locally for offline access and opens it for viewing.
Browser Automation: Utilizes Selenium to control Chrome for demonstrating how to open a URL programmatically.

Technologies Used
requests: For making HTTP requests.
beautifulsoup4: For parsing HTML and extracting data.
selenium: For browser automation.
csv: For data storage in CSV format.
webbrowser: For opening local files in a web browser.
webdriver_manager: For managing the browser driver.
How to Run
To run these scripts:

Ensure you have Python installed along with the necessary libraries (requests, beautifulsoup4, selenium, webdriver_manager).
Clone this repository to your local machine.
Navigate to the directory containing the scripts and execute them using Python. For example:
bash
Copy
python dunkin_donuts_menu_scraper.py
Setup
Before running the scripts, install all required Python packages using pip:

bash
Copy
pip install requests beautifulsoup4 selenium webdriver_manager
Results
Upon execution, each script will:

Scrape Dunkin' Donuts Menu: Outputs a CSV file named dunkin_donuts_menu.csv containing the extracted menu items.
Save and View HTML Locally: Saves the HTML file dunkin_donuts.html and opens it in Chrome.
Open Menu URL in Chrome: Opens the Dunkin' Donuts menu webpage in a new Chrome window.