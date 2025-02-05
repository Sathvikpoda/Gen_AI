Web Content to PDF Scraper

This repository contains a Python script that scrapes web content from specified URLs and saves the content as PDF files. This script is particularly useful for capturing and archiving web pages for offline reading or documentation purposes.

Description
The script operates in several steps: It reads URLs from a text file, scrapes the title and initial content from each URL using requests and BeautifulSoup, and then saves the extracted information to individual PDF files using FPDF.

Key Features
URL Reading: Extracts URLs from a specified text file.
Content Scraping: Fetches web pages and extracts the title and the first few paragraphs of content.
PDF Generation: Converts the scraped content into PDF format and saves it under a sanitized title derived from the web page's title.
Error Handling: Manages HTTP errors and exceptions gracefully, providing feedback on the success or failure of web scraping attempts.
Technologies Used
requests: For making HTTP requests to retrieve web pages.
beautifulsoup4: For parsing HTML and extracting data.
FPDF: For generating PDF files from scraped content.
re: For sanitizing titles to create valid filenames.

How to Run
To run this script:

Ensure you have Python installed along with the necessary libraries (requests, beautifulsoup4, and fpdf).
Download or clone this repository to your local machine.
Place the URLs you want to scrape in a text file named links.txt, each URL on a new line.

Run the script from your terminal or command prompt:
python web_to_pdf_scraper.py
Setup
Before running the script, install all required Python packages using pip:
pip install requests beautifulsoup4 fpdf

Results
Upon execution, the script will:

Read each URL from the links.txt file.
Attempt to scrape each URL for its title and content.
Convert the content to PDF format and save it under a filename derived from the title of the web page.
Print a message for each URL processed, indicating success or reporting any issues encountered.