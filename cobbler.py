import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    url = 'https://www.cobbler.nl/werken-bij-cobbler'  # Updated URL

    try:
        driver = get_driver()
        driver.get(url)

        p_elements = driver.find_elements(By.CSS_SELECTOR, 'p')  # Find <p> elements
        text_list = []

        for p in p_elements:
            p_text = p.text.strip()  # Get the text content of the <p> element
            if p_text:  # Check if the text is not empty
                text_list.append(p_text)

        driver.quit()

        unwanted_keywords = ['085) 024 0800', 'vacature', 'probleem', 'collega', 'werken', 'vestigingen']

        cleaned_list = [item for item in text_list if not any(keyword in item.lower() for keyword in unwanted_keywords) and item.strip()]

        with open('credentials.json', 'r') as creds_file:
            credentials = json.load(creds_file)

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_key = '1EMECLMuTk6WD6Zn1kQHCM8vf_Cgmb6yFknt_fild_xo'
        worksheet_name = 'Blad1'
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

        # Change row to 25
        row_number = 57

        worksheet.update_cell(row_number, 1, url)  # Updated to row 25
        for i, item in enumerate(cleaned_list, start=1):
            worksheet.update_cell(row_number, i + 1, item)  # Updated to row 25 if item is not empty
            print(f"Added item {i}: {item}")

        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        current_datetime_amsterdam = datetime.now(amsterdam_tz)

        worksheet.update_cell(row_number, len(cleaned_list) + 2, current_datetime_amsterdam.strftime("%Y-%m-%d"))  # Updated to row 25
        worksheet.update_cell(row_number, len(cleaned_list) + 3, current_datetime_amsterdam.strftime("%H:%M:%S"))  # Updated to row 25
        print(f"Updated cell: {row_number}, {current_datetime_amsterdam.strftime('%Y-%m-%d')}")
        print(f"Updated cell: {row_number}, {current_datetime_amsterdam.strftime('%H:%M:%S')}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
