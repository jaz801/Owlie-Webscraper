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
    url = 'https://corverdevelopment.nl/vacatures/'

    try:
        driver = get_driver()
        driver.get(url)

        h3_elements = driver.find_elements(By.CSS_SELECTOR, 'h3')  # Find h3 elements

        # Create a list to store filtered h3 elements
        filtered_elements = []

        for h3 in h3_elements:
            h3_text = h3.text.strip()
            filtered_elements.append(h3_text)

        driver.quit()

        for text in filtered_elements:
            print(text)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()























