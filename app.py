from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

EMAIL = 'kisell22@yandex.ru'
PASSWORD = 'weweqasxzc123Kisel224'
PATH_TO_PROFILE = '/home/ivan/.config/google-chrome/'

options = webdriver.ChromeOptions()
options.add_argument("--allow-profiles-outside-user-dir")
options.add_argument(r"user-data-dir=/home/pashton/.config/google-chrome")
options.add_argument('enable-profile-shortcut-manager')
options.add_argument('--profile-directory=Profile 2')
# options.binary_location = "/home/pashton/Downloads/google-chrome-stable_current_amd64.deb"
driver = webdriver.Chrome(
    chrome_options=options,
    executable_path='/home/pashton/Desktop/Projects/chumba/chromedriver'
)

# url = 'https://vk.com/'

# driver.get(url=url)
# driver.close()
# driver.quit()
# /home/pashton/Downloads/google-chrome-stable_current_amd64.deb





def get_answer_captcha(sitekey, url):
    print('func is beginning')
    solver = TwoCaptcha('18b057084fb0ed2e9fa099af511eef69')
    result = solver.solve_captcha(
        site_key=sitekey,
        page_url=url,
    )
    print('ответ пришел')

    return result




# try:
time.sleep(5)
driver.get('https://login.chumbacasino.com/')
time.sleep(5)
login_input = driver.find_element(By.ID, 'login_email-input')
login_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, 'login_password-input')
password_input.send_keys(PASSWORD)
password_input.submit()
time.sleep(10)
# button_close = driver.find_element(By.ID, 'offer__close')
# button_close.click()
# time.sleep(5)
# button_close = driver.find_element(By.ID, 'offer__close')
# button_close.click()
# time.sleep(20)
print(1)
postal_code = driver.find_element(By.ID, 'footer__postal-request-code')
postal_code.click()
time.sleep(10)


get_postal_code = driver.find_element(By.ID, 'get-postal-request-code')
get_postal_code.click()
time.sleep(10)

url_sitekey = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/div/iframe').get_attribute('src')
sitekey = url_sitekey.split('&')[1][2:]
current_url = driver.current_url
answer = get_answer_captcha(sitekey, current_url)
print(answer)
time.sleep(5)
# recaptcha_responce = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/textarea')
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
key_input = driver.find_element(By.ID, 'g-recaptcha-response')
key_input.send_keys(answer)
# driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", answer)
# driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
print('введен в форму')
# driver.execute_script("document.querySelector('[id^=g-recaptcha-response]').style.display = 'block';")
time.sleep(2)
accept_no_robot = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor-label"]')
accept_no_robot.click()
# time.sleep(10)
time.sleep(100)
driver.close()
driver.quit()
#     try:
#         button_close = driver.find_element(By.ID, 'offer__close')
#         button_close.click()
#         time.sleep(10)
#
#     except:
#         pass
#
#     postal_code = driver.find_element(By.ID, 'footer__postal-request-code')
#     postal_code.click()
#
#     time.sleep(20)
#
#     get_request_code = driver.find_element(By.ID, 'get-postal-request-code')
#
#     time.sleep(20)
#
# except:
#     driver.close()
#
#
# finally:
#
#     driver.close()
