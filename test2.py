from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge("./msedgedriver")

browser.get('https://www.wikipedia.org/')

link1=browser.find_element(by=By.ID, value='js-link-box-ru')
link1.click()

assert 'Добро пожаловать' in browser.page_source
link2=browser.find_element(by=By.ID, value='Карлос_Фермин_Фицкаральд')
link2.click()

try:
    assert 'Биография' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

# Закрываем браузер
browser.close()