from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge("./msedgedriver")

browser.get('https://www.wikipedia.org/')

link1=browser.find_element(by=By.ID, value='js-link-box-ru')
link1.click()

assert 'Добро пожаловать' in browser.page_source
link2=browser.find_element(by=By.ID, value='pt-login')
link2.click()

assert 'Имя учётной записи' in browser.page_source
username=browser.find_element(by=By.ID, value='wpName1')
username.send_keys('FocusH1K1')

password=browser.find_element(by=By.ID, value='wpPassword1')
password.send_keys('12345678!a')

button=browser.find_element(by=By.ID, value='wpLoginAttempt')
button.click()

try:
    assert 'Черновик' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

# Закрываем браузер
browser.close()