#()[]_
import time, random
from selenium import webdriver
from fake_useragent import UserAgent

delay = 6
url = 'https://n5m.ru/usagent.html' #'https://www.dns-shop.ru'
# user_agent_list = []
# with open('user_agent_list.txt','r') as file:
#     for line in file.readlines():
#         user_agent_list.append(line.rstrip())
# user_agent = random.choice(user_agent_list)

useragent = UserAgent()
#options
options = webdriver.ChromeOptions()
    #options.add_argument('user-agent=Hello World :)')
    #options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 10; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36')
options.add_argument(f'user-agent={useragent.random}')
browser = webdriver.Chrome(options=options)

try:
    browser.get(url=url)
    time.sleep(delay)
    
#     browser.refresh()
#     time.sleep(delay)
    
    browser.get_screenshot_as_file('screenshot_UA.png')
#     browser.save_screenshot('screenshot_2.png')
    
except Exception as ex:
    print(ex)
    
finally:
    browser.close()
    browser.quit()