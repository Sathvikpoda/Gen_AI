Dice.com Job Scraper

This repository contains a Python script designed to scrape job listings from Dice.com based on specified roles. The script leverages Selenium for web automation to navigate through job listing pages and BeautifulSoup for parsing the HTML content to extract job details. The extracted information is saved into a CSV file for each role.

Description
The script is tailored to search for job roles such as Full Stack Developer, Frontend Developer, Backend Developer, etc., on Dice.com. It navigates through the website's pages and collects details about each job listing, including the job title, company name, location, date posted, and a link to the job description.

Key Features
Automated Browsing: Uses Selenium with a headless Chrome browser to navigate through job listings.
Data Extraction: Parses page content using BeautifulSoup to extract job details.
Data Storage: Writes the extracted data into a CSV file, making it easy to view and analyze.
Pagination Handling: Manages website pagination to continue scraping across multiple pages.

Technologies Used
selenium: For automated web browsing.
beautifulsoup4: For HTML content parsing.
csv: For storing extracted data.
time: For managing delays during navigation to ensure page elements load.

How to Run
To run this script:
Ensure you have Python installed along with the necessary libraries (selenium, beautifulsoup4, and chromedriver).
Update the path to your ChromeDriver and ensure it is correctly installed on your system.

Run the script from your terminal or command prompt:
python dice_job_scraper.py
Setup

Make sure to install all required Python packages:
pip install selenium beautifulsoup4
You will also need to download the appropriate version of ChromeDriver based on your Chrome version.

Results
Upon execution, the script:

Opens a headless Chrome browser session.
Visits Dice.com and searches for specified job roles.
Extracts job details from each listing and saves them to a CSV file named dice_full_stack_development_jobs.csv.
Handles multiple pages of job listings until no further pages are available.