import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Function to initialize and return a headless Chrome driver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    url = 'https://avinty.com/werken-bij-avinty/'  # Updated URL
    h2_contents = []  # List to store <h2> content

    try:
        driver = get_driver()
        driver.get(url)

        # Find <h2> elements with class="entry-title"
        h2_elements = driver.find_elements(By.CSS_SELECTOR, 'h2.entry-title')

        for h2_element in h2_elements:
            h2_text = h2_element.text.strip()
            if h2_text:  # Check if the content is not empty
                h2_contents.append(h2_text)  # Append content to the list

        driver.quit()

        # Print the list of <h2> contents
        for index, content in enumerate(h2_contents, start=1):
            print(f"<h2> {index}:", content)

    except Exception as e:
        print("An error occurred:", e)

# Call the main function
if __name__ == "__main__":
    main()













