#()[]_
import time
from selenium import webdriver

delay = 6
url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

#options
options = webdriver.ChromeOptions()

# useragent
useragent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' #UserAgent
options.add_argument(f'user-agent={useragent}')

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=options)

try:
    browser.get(url=url)
    time.sleep(delay)
    
    # make screenshot
    browser.get_screenshot_as_file('screenshot_disable_webdriver_mode.png')
    
except Exception as ex:
    print(ex)
    
finally:
    browser.close()
    browser.quit()