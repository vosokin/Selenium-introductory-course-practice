#()[]_
import time, pickle, user_agent_choice as UserAgent
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
browser = webdriver.Chrome(options=options)

try:
    browser.get(url=url)
    time.sleep(delay)
    
    # load cookies
    browser.delete_all_cookies()
    for cookie in pickle.load(open(f'{short_url}_{email}_cookies', 'rb')):
        browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(10 * delay)    

    # save cookies
    pickle.dump(browser.get_cookies(), open(f'{short_url}_{email}_cookies', 'wb'))
 
except Exception as ex:
    print(ex)
    
finally:
    browser.close()
    browser.quit()