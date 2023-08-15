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
    url = 'https://careers.bringme.com/'  # Updated URL

    try:
        driver = get_driver()
        driver.get(url)

        div_elements = driver.find_elements(By.CLASS_NAME, 'sc-1543tgf-2')  # Find all <div> elements with class name
        stored_items = []

        for div in div_elements:
            div_text = div.text.strip()
            if div_text:
                stored_items.append(div_text)

        driver.quit()

        with open('credentials.json', 'r') as creds_file:
            credentials = json.load(creds_file)

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_key = '1EMECLMuTk6WD6Zn1kQHCM8vf_Cgmb6yFknt_fild_xo'
        worksheet_name = 'Blad1'
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

        # Change row to 41
        row_number = 41

        worksheet.update_cell(row_number, 1, url)  # Updated to row 41
        for i, item in enumerate(stored_items, start=1):
            worksheet.update_cell(row_number, i + 1, item)  # Updated to row 41 if item is not empty
            print(f"Added item {i}: {item}")

        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        current_datetime_amsterdam = datetime.now(amsterdam_tz)

        worksheet.update_cell(row_number, len(stored_items) + 2, current_datetime_amsterdam.strftime("%Y-%m-%d"))  # Updated to row 41
        worksheet.update_cell(row_number, len(stored_items) + 3, current_datetime_amsterdam.strftime("%H:%M:%S"))  # Updated to row 41
        print(f"Updated cell: {row_number}, {current_datetime_amsterdam.strftime('%Y-%m-%d')}")
        print(f"Updated cell: {row_number}, {current_datetime_amsterdam.strftime('%H:%M:%S')}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()