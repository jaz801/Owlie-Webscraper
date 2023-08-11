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
    # Replace this URL with the website you want to scrape
    url = 'https://booqi.me/werken-bij/'

    try:
        driver = get_driver()
        driver.get(url)

        div_elements = driver.find_elements(By.XPATH, '//div[@class="brz-css-jujqz brz-wrapper"]')
        
        # Initialize an empty list to store the span elements' text
        span_elements_text_list = []

        for div in div_elements:
            span_elements = div.find_elements(By.TAG_NAME, 'span')
            for span_element in span_elements:
                span_text = span_element.text.strip()
                if span_text and span_text.isupper():
                    span_elements_text_list.append(span_text)
                    print(span_text)

        # Define the credentials directly in the code as a dictionary
        credentials = {
            # Add your credentials here
            "type": "service_account",
            "project_id": "watchful-force-389009",
            "private_key_id": "a55b9a4d6e46ec84ea082eecb51e5a866f1a0abc",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC76WVjpitE6IGh\nhbshkXOeepRgzvVzI3LwY4n/U/pfK0+YH70hStBhHqCPbO5E/I3V4s2YRP+7ugFG\n710TXusFvwiANLaSZXACgVAwAiRvJE1UM6QBVkU9ouwtWli0TN/GdCwVPSoLQCYj\nd3AN/scMzp1CuwoG0uSIx+rYt5yLryrZkFFw27rrvZVzuF3oqeVOEDtlEYRwHazd\nOO08i8wyFNfqGpmhD9U3udgMcMhr0GqYgm6rq78iqXEM4cr+ipIUpJe5C9AwhHXM\niy+sb1CkaD7K7mZHMcBDiNo/p9cfMBTnGYcYF2oe1VRYyz5wK1u+1dbWWoIlRHCR\nhjJRHzlvAgMBAAECggEAAhfVc0i0jq3wU7ZDoVoXaZp/8Jwdi8zHSPoy3U84KLs4\nxb8EwkwtCgfnTfGurcIKaml+VMXf+11VCk88QCz8fTHljFgJ+JN8rep21DIR6dMD\nsX5pw0IMv2UDMHYjKs74ZyOAIjRuNXXfduGrs9w0p2XdxpKCyBStSwC/Eu7opX2n\nGXRMSVKocO8gXX5xVjW8iw37HU7aTQT8lrdAuSxh3CeUixfVgLjOP47LIDJzqgAP\ncP1/XkSQ5fBSqhmw/GLgCph7+2RLS8RN172kMSCnsbFcgokE/dzh9CiRbFV+wOzI\nU+oOjCj9vY624r/3ryMWznSfkHqIz5E2v6wcc6TgIQKBgQDyUVtoToPaZVQOdbRU\ni4vb8yvOr1024a9rRNFXdJscN57JPiW5cNpZIlkGZqTtR/GaNMpQSlKuFV76p7ae\nyuF2w7nfax6OgFBUB/7VbPFGohCMeDI15pDEp8cNjXfMjKH5LDJyjyOgH8S2xOBw\neSsUnd064TuSq0slERhak4z85wKBgQDGhZzN6ecKDIaHed/5tGmFOFdj12GtsFim\nsmkvO0dLfoPXBwCXDQhBvgsDGPgXTKV/XRPfVtm1smLMg+d10YR8SmuRxcOidLo7\nAFh5ij3tIYi4q/lfwt1db2NC6UYajoJydKF7j20pMLPhGODVSuTxuKrACtQjV5kY\nsTkyTZaGOQKBgQDE9xqc241TvZ+orUZqno+Ntsi6FVNoo+QqBmM/eloGgrOAExMo\n/DGP2FqS2GZhNWSOmzCEORWhyV9N0Xug8Xp5RjlVAMZywJwK4gDjTM2GQ3++Hol5\nxLOSFmq3enGRhBK47pMHCZDEvG3yvm9NHUDGXleQX7pDyxamx5GLNnqYqwKBgCyj\nPm7OeTS5PEaaENKEznU2BfBdLYlwbX6N/zivi4heGibvXCKau5CMus0ngCE9Crlo\npF9DmBBS3ARAZHsJcVDBKw7L+QE+XeGGYl5xxxrav3NGt/vgRQYNVbRl3215Pbue\nnfC6f0ETwl6KyYMsI+52J26nAKwxtirnLoUxDPeBAoGAYw6WbDwVBEYH+W+Bs3XH\nDSDij3NlfxxB3h+y+J57s3ZADoWD/X/ANiT3dBHd/WTDIjZsorcX6FlncgDG/MjB\nG91yzc",
            "client_email": "jasper-ruijs@watchful-force-389009.iam.gserviceaccount.com",
            "client_id": "113552177275791885843",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/jasper-ruijs%40watchful-force-389009.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }

        # Push the data to Google Sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_key = '1EMECLMuTk6WD6Zn1kQHCM8vf_Cgmb6yFknt_fild_xo'
        worksheet_name = 'Blad1'  # Replace with the name of your sheet
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

        # Replace this with the desired row number
        row_number = 12

        # Write the data to the sheet
        worksheet.update_cell(row_number, 1, url)
        for i, span_text in enumerate(span_elements_text_list, start=1):
            worksheet.update_cell(row_number, i + 1, span_text)
            print(f"Added span element {i}: {span_text}")

        # Convert the current time to Amsterdam timezone
        amsterdam_timezone = pytz.timezone('Europe/Amsterdam')
        current_datetime_amsterdam = datetime.now(amsterdam_timezone)

        # Update the adjacent cells with the current date and time in Amsterdam timezone
        date_cell = worksheet.cell(row_number, len(span_elements_text_list) + 2)
        time_cell = worksheet.cell(row_number, len(span_elements_text_list) + 3)

        date_cell.value = current_datetime_amsterdam.strftime("%Y-%m-%d")
        time_cell.value = current_datetime_amsterdam.strftime("%H:%M:%S")

        worksheet.update_cells([date_cell, time_cell])

        print(f"Updated cell: {len(span_elements_text_list) + 2}, {current_datetime_amsterdam.strftime('%Y-%m-%d')}")
        print(f"Updated cell: {len(span_elements_text_list) + 3}, {current_datetime_amsterdam.strftime('%H:%M:%S')}")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

















        
