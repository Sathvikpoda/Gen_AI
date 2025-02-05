YouTube Comments Scraper

This repository contains a Python script that automates the process of scraping comments from a YouTube video using Selenium. The script navigates to a specified YouTube video, loads the comments section by simulating scrolling, and extracts comments and their corresponding authors, saving the data to a CSV file.

Description
The script uses Selenium WebDriver to interact with YouTube’s interface, effectively loading comments by scrolling down the video's comment section and capturing the text and author of each comment. The comments are then stored in a CSV file for further analysis or archiving purposes.

Key Features
Headless Mode: Supports running in headless mode to avoid opening a browser window during the scraping process.
Data Extraction: Gathers both the comment text and the author's name for each comment.
Data Storage: Outputs the collected comments and authors to a CSV file.
Technologies Used
selenium: For browser automation to interact with the YouTube page.
csv: For writing the extracted data to a CSV file.
webdriver_manager: For managing the browser driver automatically.

How to Run
To run this script:

Ensure you have Python installed along with the necessary libraries (selenium and webdriver_manager).
Download or clone this repository to your local machine.
Update the video_url variable in the script to the URL of the YouTube video from which you want to scrape comments.
Specify the output_csv filename for where you want the comments to be saved.
Run the script from your terminal or command prompt:
python youtube_comments_scraper.py
Setup

Before running the script, make sure to install all required Python packages using pip:
pip install selenium webdriver_manager

Results
Upon execution, the script will:

Navigate to the specified YouTube video.
Automatically scroll through the comment section to load comments.
Extract the text and author of each comment.
Save the comments and author names to the specified CSV file.
Print the number of comments scraped and the location of the saved CSV file to the console.