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
    url = 'https://www.arcadiz.com/en/jobs'  # Updated URL
    h3_contents = []  # List to store <h3> content

    try:
        driver = get_driver()
        driver.get(url)

        h3_elements = driver.find_elements(By.CSS_SELECTOR, 'h3')  # Find <h3> elements

        for h3_element in h3_elements:
            h3_text = h3_element.text.strip()
            h3_contents.append(h3_text)  # Append content to the list

        driver.quit()

        # Print the list of <h3> contents
        for index, content in enumerate(h3_contents, start=1):
            print(f"<h3> {index}:", content)

    except Exception as e:
        print("An error occurred:", e)

# Call the main function
if __name__ == "__main__":
    main()









