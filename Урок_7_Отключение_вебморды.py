#()[]_
import time, pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import email, password

delay = 6
url = 'https://vk.ru'
short_url = url.split('//')[1]

#options
options = webdriver.ChromeOptions()

# useragent
useragent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' #UserAgent
options.add_argument(f'user-agent={useragent}')

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)

try:
    browser.get(url=url)
    time.sleep(delay)
    
    # email_input
    email_input = browser.find_element(by=By.XPATH, value='//input[@id="index_email"]')
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(delay)
    
    # click button
    button_click = browser.find_element(by=By.XPATH, value='//button[@type="submit"]').click()
    time.sleep(2 * delay)    
    
    # password_input
    password_input = browser.find_element(by=By.XPATH, value='//*[@name="password"]')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(delay)

    # click button
    button_click = browser.find_element(by=By.XPATH, value='//button[@type="submit"]').click()
    time.sleep(10 * delay)    
    
    # save cookies
    pickle.dump(browser.get_cookies(), open(f'{short_url}_{email}_cookies', 'wb'))
    
    # make site-authentication screenshot
    browser.save_screenshot(f'{short_url}_{email}_screenshot.png')
    
except Exception as ex:
    print(ex)
    
finally:
    browser.close()
    browser.quit()