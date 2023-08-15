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
    url = 'https://jobs.askphill.com/?selectedType=department&'  # Updated URL

    try:
        driver = get_driver()
        driver.get(url)

        p_elements = driver.find_elements(By.CSS_SELECTOR, 'p.JobListItems__jobTitle__NPxUU')  # Find <p> elements with class "JobListItems__jobTitle__NPxUU"
        stored_items = []

        for p in p_elements:
            p_text = p.text.strip()

            if p_text:
                stored_items.append(p_text)

        driver.quit()

        with open('credentials.json', 'r') as creds_file:
            credentials = json.load(creds_file)
            print("Loaded credentials:", credentials)  # Debugging line

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_key = '1EMECLMuTk6WD6Zn1kQHCM8vf_Cgmb6yFknt_fild_xo'
        worksheet_name = 'Blad1'
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

        worksheet.update_cell(17, 1, url)
        for i, item in enumerate(stored_items, start=1):
            worksheet.update_cell(17, i + 1, item)  # Change row 16 to 17
            print(f"Added item {i}: {item}")

        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        current_datetime_amsterdam = datetime.now(amsterdam_tz)

        worksheet.update_cell(17, len(stored_items) + 2, current_datetime_amsterdam.strftime("%Y-%m-%d"))  # Change row 16 to 17
        worksheet.update_cell(17, len(stored_items) + 3, current_datetime_amsterdam.strftime("%H:%M:%S"))  # Change row 16 to 17
        print(f"Updated cell: {len(stored_items) + 2}, {current_datetime_amsterdam.strftime('%Y-%m-%d')}")
        print(f"Updated cell: {len(stored_items) + 3}, {current_datetime_amsterdam.strftime('%H:%M:%S')}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

