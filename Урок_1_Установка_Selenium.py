#()
from selenium import webdriver
import time

delay = 6
url = 'https://www.dns-shop.ru'
browser = webdriver.Chrome()

try:
    browser.get(url=url)
    time.sleep(delay)
    
#     browser.refresh()
#     time.sleep(delay)
    
#     browser.get_screenshot_as_file('screenshot_1.png')
#     browser.save_screenshot('screenshot_2.png')
    
except Exception as ex:
    print(ex)
    
finally:
    browser.close()
    browser.quit()