import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz

def main():
    # Replace this URL with the website you want to scrape
    url = "https://werkenbij.adver-online.nl/vacatures"

    # Send a GET request to the website and get the content
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch the content. Status code: {response.status_code}")
        return

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <h5> tags with class="card-title"
    h5_elements = soup.find_all('h5', class_='card-title')

    # Initialize an empty list to store the h5 elements' text
    h5_elements_text_list = []

    # Loop through each h5_element and extract the text
    for h5_element in h5_elements:
        h5_elements_text_list.append(h5_element.text.strip())

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
    worksheet.update_cell(4, 1, 'https://werkenbij.adver-online.nl/')
    for i, h5_text in enumerate(h5_elements_text_list, start=1):
        worksheet.update_cell(4, i+1, h5_text)
        print(f"Added h5 element {i}: {h5_text}")

    # Get the current time in UTC
    current_time_utc = datetime.now(pytz.utc)

    # Convert to Amsterdam timezone
    amsterdam_tz = pytz.timezone('Europe/Amsterdam')
    current_time_amsterdam = current_time_utc.astimezone(amsterdam_tz)
    current_date = current_time_amsterdam.strftime("%Y-%m-%d")
    current_time = current_time_amsterdam.strftime("%H:%M:%S")

    # Update the adjacent cells with the current date and time in Amsterdam timezone
    worksheet.update_cell(4, len(h5_elements_text_list) + 2, current_date)
    worksheet.update_cell(4, len(h5_elements_text_list) + 3, current_time)
    print(f"Updated cell: {len(h5_elements_text_list) + 2}, {current_date}")
    print(f"Updated cell: {len(h5_elements_text_list) + 3}, {current_time}")

if __name__ == "__main__":
    main()
