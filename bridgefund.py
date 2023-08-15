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
    url = 'https://www.bridgefund.nl/bedrijf/vacatures/#rt-jobs-1'  # Change URL

    try:
        driver = get_driver()
        driver.get(url)

        span_elements = driver.find_elements(By.CLASS_NAME, 'rt-list__offer-title')  # Find all <span> elements with class "rt-list__offer-title"
        stored_items = []

        for span in span_elements:
            span_text = span.text.strip()
            if span_text:
                stored_items.append(span_text)

        driver.quit()

        with open('credentials.json', 'r') as creds_file:
            credentials = json.load(creds_file)

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_key = '1EMECLMuTk6WD6Zn1kQHCM8vf_Cgmb6yFknt_fild_xo'
        worksheet_name = 'Blad1'
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

        # Change row to 38
        row_number = 38

        worksheet.update_cell(row_number, 1, url)  # Updated to row 38
        for i, item in enumerate(stored_items, start=1):
            worksheet.update_cell(row_number, i + 1, item)  # Updated to row 38 if item is not empty
            print(f"Added item {i}: {item}")

        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        current_datetime_amsterdam = datetime.now(amsterdam_tz)

        worksheet.update_cell(row_number, len(stored_items) + 2, current_datetime_amsterdam.strftime("%Y-%m-%d"))  # Updated to row 38
        worksheet.update_cell(row_number, len(stored_items) + 3, current_datetime_amsterdam.strftime("%H:%M:%S"))  # Updated to row 38
        print(f"Updated cell: {row_number}, {current_datetime_amsterdam.strftime('%Y-%m-%d')}")
        print(f"Updated cell: {row_number}, {current_datetime_amsterdam.strftime('%H:%M:%S')}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
