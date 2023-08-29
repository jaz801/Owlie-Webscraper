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
    url = 'https://werkenbijcloudwise.nl/'  # Updated URL

    try:
        driver = get_driver()
        driver.get(url)

        div_elements = driver.find_elements(By.CSS_SELECTOR, 'div.sc-123pquh-2.iKddul')  # Find <div> elements with the specified class
        stored_items = []

        for div_element in div_elements:
            div_text = div_element.text.strip()

            if div_text:
                stored_items.append(div_text)
                print("<div> content:", div_text)

        driver.quit()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()






