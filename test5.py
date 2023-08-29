from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    urls = [
        'https://www.carcomplaints.com/Ford/Focus/2012/accessories-interior/horn_disabled.shtml',
        'https://www.carcomplaints.com/Ford/Focus/2012/body_paint/door_opened_while_driving.shtml',
        'https://www.carcomplaints.com/Ford/Focus/2012/suspension/alignment_issue.shtml'
    ]

    try:
        driver = get_driver()
        
        with open('car_data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            for url in urls:
                driver.get(url)

                # Print the current URL
                print("Current URL:")
                print(driver.current_url)

                try:
                    vheader_div = driver.find_element(By.ID, "vheader")
                    h1_element = vheader_div.find_element(By.TAG_NAME, "h1")
                    print("Content of <h1> element:")
                    print(h1_element.text)
                except NoSuchElementException:
                    print("Failed to find vheader_div or h1_element")

                try:
                    psolutions_div = driver.find_element(By.ID, "psolutions")
                    ol_element = psolutions_div.find_element(By.TAG_NAME, "ol")
                    print("\nContent of <ol> element:")
                    print(ol_element.text)
                except NoSuchElementException:
                    print("Failed to find psolutions_div or ol_element")

                # Store information in the CSV file
                csvwriter.writerow([url, h1_element.text, ol_element.text])
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

