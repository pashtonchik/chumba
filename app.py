from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--allow-profiles-outside-user-dir")
options.add_argument(r"user-data-dir=/home/pashton/.config/google-chrome")
options.add_argument('enable-profile-shortcut-manager')
options.add_argument('--profile-directory=Profile 1')
# options.binary_location = "/home/pashton/Downloads/google-chrome-stable_current_amd64.deb"
driver = webdriver.Chrome(
    chrome_options=options,
    executable_path='/home/pashton/Desktop/Projects/chumba/chromedriver'
)

url = 'https://vk.com/'

driver.get(url=url)
# driver.close()
# driver.quit()
# /home/pashton/Downloads/google-chrome-stable_current_amd64.deb