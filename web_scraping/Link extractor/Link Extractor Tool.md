Link Extractor Tool

This repository contains a Python script that extracts all hyperlinks from a specified webpage and saves them to a text file. It's designed to handle both absolute and relative URLs, converting them to full URLs before saving.

Description
The script uses the requests library to fetch the content of the webpage and the BeautifulSoup library to parse the HTML. It identifies all anchor tags (<a>) with an href attribute, extracts the URLs, and saves them into a text file.

Key Features
URL Fetching: Sends a GET request to retrieve the webpage.
Link Extraction: Parses the page to find all links and handles conversion of relative links to absolute.
File Output: Saves the list of URLs to a text file, ensuring each link is on a new line.
Technologies Used
requests: For sending HTTP requests.
beautifulsoup4: For parsing HTML content.
urllib.parse: For converting relative URLs to absolute URLs.

How to Run
To run this script:
Ensure you have Python installed along with the necessary libraries (requests, beautifulsoup4).
Update the url variable in the script to the webpage from which you want to extract links.
Specify the filename in which you want the links to be saved or use the default links.txt.
Run the script from your terminal or command prompt:
python link_extractor.py

Setup
Before running the script, make sure to install all required Python packages using pip:
pip install requests beautifulsoup4

Results
Upon execution, the script will:
Retrieve and parse the specified webpage.
Extract all links and save them to the specified text file.
Provide a status message indicating success or failure along with the number of links found and saved.
