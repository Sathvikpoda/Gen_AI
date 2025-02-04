from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Set up Chrome options
options = Options()
# options.add_argument("--headless")  # Comment this for debugging
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Setup Chrome service
service = Service(ChromeDriverManager().install())

# Initialize the driver with the service and options
driver = webdriver.Chrome(service=service, options=options)

try:
    # URL of the job listing page
    driver.get('https://www.monster.com/jobs/search?q=GEN+AI&where=&page=1&so=m.s.sh')
    wait = WebDriverWait(driver, 30)  # Increased wait time for dynamic content

    # Using visibility_of_all_elements_located to ensure elements are interactable
    jobs = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.card-content > a[href]")))  # Updated selector

    # Extract href attributes to get the job links
    job_links = [job.get_attribute('href') for job in jobs]

    # Write job links to a CSV file
    with open('job_links.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Link'])
        for link in job_links:
            writer.writerow([link])

    print(f"Successfully scraped {len(job_links)} job links.")

finally:
    driver.quit()  # Ensure the driver quits regardless of success or failure
