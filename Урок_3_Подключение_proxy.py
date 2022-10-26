#()[]_
import time, random
from selenium import webdriver
from fake_useragent import UserAgent

delay = 6
url = 'https://whoer.net' #'https://www.dns-shop.ru'
useragent = UserAgent()
proxy = '176.192.70.58:8001'

#options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.random}')

#set proxy
options.add_argument('--proxy-server=176.192.70.58:8001')

browser = webdriver.Chrome(options=options)

try:
    browser.get(url=url)
    time.sleep(delay)
    browser.get_screenshot_as_file('screenshot_UA.png')
    
except Exception as ex:
    print(ex)
    
finally:
    browser.close()
    browser.quit()