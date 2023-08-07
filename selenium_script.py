from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.youtube.com/watch?v=FcW-AXsirBE&ab_channel=Jovian'

def get_driver():
 chrome_options = Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--headless')
 chrome_options.add_argument('--disable-dev-shm-usage')
 driver = webdriver.Chrome(options=chrome_options)
 return driver

if __name__== "__main__":
  driver = get_driver()
  driver.get(url)
  print('page title',driver.title)
 