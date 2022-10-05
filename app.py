from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/home/pashton/Downloads/google-chrome-stable_current_amd64.deb"
driver = webdriver.Chrome(executable_path='/home/pashton/Desktop/Projects/chumba/chromedriver')

url = 'https://vk.com/'

driver.get(url=url)
driver.close()
driver.quit()
# /home/pashton/Downloads/google-chrome-stable_current_amd64.deb