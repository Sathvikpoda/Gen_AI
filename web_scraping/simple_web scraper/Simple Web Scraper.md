Simple Web Scraper

This repository contains a Python script that scrapes text content from a specified webpage using the requests library for HTTP requests and BeautifulSoup for parsing HTML content. The extracted text is then saved to a text file.

Description
The script is designed to retrieve all paragraph elements (<p> tags) from a given webpage, extract their text content, and save it in a simple text file. This tool is useful for collecting textual data from websites for research, analysis, or backup purposes.

Key Features
HTTP Requests: Uses the requests library to fetch webpages.
HTML Parsing: Utilizes BeautifulSoup to parse the HTML content and extract text.
Text Extraction: Gathers all text contained within paragraph tags of the webpage.
File Output: Writes the extracted text to a specified file.
Technologies Used
requests: For sending HTTP requests to retrieve webpages.
beautifulsoup4: For parsing HTML and extracting data.
How to Run
To run this script:

Ensure you have Python installed along with the necessary libraries (requests and beautifulsoup4).
Download or clone this repository to your local machine.
Update the url variable in the script to the URL from which you want to scrape text.
Optionally, change the filename variable to specify the name of the output file.

Run the script from your terminal or command prompt:
python scraper.py
Setup

Before running the script, install all required Python packages using pip:
pip install requests beautifulsoup4
Results
Upon execution, the script will:

Fetch the specified webpage.
Extract all text from paragraph elements.
Save the extracted text to the specified file.
Print a message indicating the successful retrieval and saving of content, or report any errors encountered during the process.