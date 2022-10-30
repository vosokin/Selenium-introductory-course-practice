import time, pickle, os
from selenium import webdriver
from selenium.webdriver.common.by import By

delay = 6
links = []
product = 'кроссовки'
region = 'moskva'
url = f'https://www.avito.ru/{region}?q={product}'
print(f'Полный URL: {url}')
short_url = url.split('//')[1].split('/')[0]
if 'www' in short_url:
    short_url = short_url.lstrip('www.')

options = webdriver.ChromeOptions()
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 YaBrowser/20.12.0.963 Yowser/2.5 Safari/537.36'
options.add_argument(f'user-agent={useragent}')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

try:
    # navigate to a website
    print(f'Загружаю сайт в браузер.')
    browser.get(url=url)    
    browser.implicitly_wait(delay * 10)
    
    # work with items (photos)
    print(f'Работаю с элементами 1й страницы.')
    items = browser.find_elements(by=By.XPATH, value="//a[contains(@class,'iva-item-sliderLink')]")
    browser.implicitly_wait(delay * 10)
    print(f'Количество элементов на странице: {len(items)}')
    for item in items:
        links.append(item.get_property('href').rstrip())
        #print(links[-1])
    browser.implicitly_wait(delay)
    
    # navigate to a link
    print(f"Загружаю {links[0]} в браузер.")
    items[0].click()
    browser.implicitly_wait(delay * 10)
    
    # switch to next window
    print(f"Перехожу на окно {items[0].get_property('href')}.")
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(delay)
    print(f"Текущий URL: {browser.current_url}")
    browser.maximize_window()
    
    # scroll window down
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # make site screenshot
    filename = f"{short_url}_{browser.current_url.split('_')[-1]}_screenshot.png"
    print(f"Делаю скриншот {browser.current_url} и сохраняю его в файл {filename}.")
    browser.save_screenshot(f'{filename}')
    
except Exception as ex:
    print('#' * 60)
    print(f'\nВнимание! в скрипте ошибка:\n{ex}\n')
    print('#' * 60)
    
finally:
    print('Закрываю браузер.')
    browser.close()    
    browser.quit()
    print('Браузерная сессия закрыта.')

# open file with screenshot
print('Открываю файл скриншота.')
os.system(f'{filename}')
    
print('=' * 60)