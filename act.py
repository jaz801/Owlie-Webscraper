from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://careers.actcommodities.com/global/en/search-results?category=Facilities'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

if __name__ == "__main__":
    driver = get_driver()
    driver.get(url)

    # Find the parent <div> with class name 'panel-body au-target'
    parent_div = driver.find_element(By.CSS_SELECTOR, 'div.panel-body.au-target')

    # Find all the nested <span> elements with class name 'checkbox'
    checkboxes = parent_div.find_elements(By.CSS_SELECTOR, 'span.checkbox')

    print(f"Found {len(checkboxes)} checkboxes.")

    # Iterate through the first 12 checkboxes and click using explicit waits
    for index, checkbox in enumerate(checkboxes[:12], start=1):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.checkbox')))
        checkbox.click()
        print(f"Clicked on checkbox {index}/12.")

    print("Finished clicking on checkboxes.")

    # Wait for user input before closing the browser window
    input("Press Enter to close the browser...")

    # Close the browser window
    driver.quit()




        