import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz

# Function to fetch the HTML content of the web page
def get_html_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Function to parse the HTML content using BeautifulSoup and extract all the <a> tags' text within the desired divs
def extract_a_text_within_divs(html_content, target_class):
    soup = BeautifulSoup(html_content, 'html.parser')
    div_elements = soup.find_all('div', class_=target_class)
    a_texts = []
    for div_element in div_elements:
        a_elements = div_element.find_all('a')
        a_texts.extend(a.get_text() for a in a_elements)
    return a_texts

def main():
    # Replace 'YOUR_URL_HERE' with the actual URL of the web page you want to scrape
    url = 'https://careers.aimms.com/'
    target_class = 'sc-1543tgf-2 hRnmvn'

    try:
        html_content = get_html_content(url)
        a_texts = extract_a_text_within_divs(html_content, target_class)

        if a_texts:
            print(f"The text content of <a> tags within divs with class '{target_class}':")
            for idx, text in enumerate(a_texts, 1):
                print(f"{idx}. {text}")
        else:
            print(f"No <a> tags found within divs with class '{target_class}'.")

        # Define the credentials directly in the code as a dictionary
        credentials = {
            # Add your credentials here
            "type": "service_account",
            "project_id": "watchful-force-389009",
            "private_key_id": "a55b9a4d6e46ec84ea082eecb51e5a866f1a0abc",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC76WVjpitE6IGh\nhbshkXOeepRgzvVzI3LwY4n/U/pfK0+YH70hStBhHqCPbO5E/I3V4s2YRP+7ugFG\n710TXusFvwiANLaSZXACgVAwAiRvJE1UM6QBVkU9ouwtWli0TN/GdCwVPSoLQCYj\nd3AN/scMzp1CuwoG0uSIx+rYt5yLryrZkFFw27rrvZVzuF3oqeVOEDtlEYRwHazd\nOO08i8wyFNfqGpmhD9U3udgMcMhr0GqYgm6rq78iqXEM4cr+ipIUpJe5C9AwhHXM\niy+sb1CkaD7K7mZHMcBDiNo/p9cfMBTnGYcYF2oe1VRYyz5wK1u+1dbWWoIlRHCR\nhjJRHzlvAgMBAAECggEAAhfVc0i0jq3wU7ZDoVoXaZp/8Jwdi8zHSPoy3U84KLs4\nxb8EwkwtCgfnTfGurcIKaml+VMXf+11VCk88QCz8fTHljFgJ+JN8rep21DIR6dMD\nsX5pw0IMv2UDMHYjKs74ZyOAIjRuNXXfduGrs9w0p2XdxpKCyBStSwC/Eu7opX2n\nGXRMSVKocO8gXX5xVjW8iw37HU7aTQT8lrdAuSxh3CeUixfVgLjOP47LIDJzqgAP\ncP1/XkSQ5fBSqhmw/GLgCph7+2RLS8RN172kMSCnsbFcgokE/dzh9CiRbFV+wOzI\nU+oOjCj9vY624r/3ryMWznSfkHqIz5E2v6wcc6TgIQKBgQDyUVtoToPaZVQOdbRU\ni4vb8yvOr1024a9rRNFXdJscN57JPiW5cNpZIlkGZqTtR/GaNMpQSlKuFV76p7ae\nyuF2w7nfax6OgFBUB/7VbPFGohCMeDI15pDEp8cNjXfMjKH5LDJyjyOgH8S2xOBw\neSsUnd064TuSq0slERhak4z85wKBgQDGhZzN6ecKDIaHed/5tGmFOFdj12GtsFim\nsmkvO0dLfoPXBwCXDQhBvgsDGPgXTKV/XRPfVtm1smLMg+d10YR8SmuRxcOidLo7\nAFh5ij3tIYi4q/lfwt1db2NC6UYajoJydKF7j20pMLPhGODVSuTxuKrACtQjV5kY\nsTkyTZaGOQKBgQDE9xqc241TvZ+orUZqno+Ntsi6FVNoo+QqBmM/eloGgrOAExMo\n/DGP2FqS2GZhNWSOmzCEORWhyV9N0Xug8Xp5RjlVAMZywJwK4gDjTM2GQ3++Hol5\nxLOSFmq3enGRhBK47pMHCZDEvG3yvm9NHUDGXleQX7pDyxamx5GLNnqYqwKBgCyj\nPm7OeTS5PEaaENKEznU2BfBdLYlwbX6N/zivi4heGibvXCKau5CMus0ngCE9Crlo\npF9DmBBS3ARAZHsJcVDBKw7L+QE+XeGGYl5xxxrav3NGt/vgRQYNVbRl3215Pbue\nnfC6f0ETwl6KyYMsI+52J26nAKwxtirnLoUxDPeBAoGAYw6WbDwVBEYH+W+Bs3XH\nDSDij3NlfxxB3h+y+J57s3ZADoWD/X/ANiT3dBHd/WTDIjZsorcX6FlncgDG/MjB\nG91yzc0+9szCoRrwViCbAHv6ngOCosLxxaGVXnv+oWewB/ZAtjZwAE4JQTpVC1vY\ngHse2zcBUbXjvH6Q98L2T+s=\n-----END PRIVATE KEY-----\n",
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

        # Write the data to the sheet
        worksheet.update_cell(8, 1, url)
        for i, a_text in enumerate(a_texts, start=1):
            worksheet.update_cell(8, i+1, a_text)
            print(f"Added <a> tag {i}: {a_text}")

        # Convert time to Amsterdam timezone
        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        current_datetime = datetime.now(amsterdam_tz)
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S")

        # Update the adjacent cells with the current date and time in Amsterdam timezone
        worksheet.update_cell(8, len(a_texts) + 2, current_date)
        worksheet.update_cell(8, len(a_texts) + 3, current_time)
        print(f"Updated cell: {len(a_texts) + 2}, {current_date}")
        print(f"Updated cell: {len(a_texts) + 3}, {current_time}")

    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()