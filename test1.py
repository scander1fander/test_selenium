from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge("./msedgedriver")
browser.get('https://www.wikipedia.org/')

name=browser.find_element(by=By.NAME, value='search')
name.send_keys('Щедрин, Родион Константинович')

button=browser.find_element(by=By.CSS_SELECTOR, value='.search-container button')
button.click()

try:
    assert "Щедрин, Родион Константинович" in browser.page_source
    print('The text was completed successfully')
except Exception as err:
    print('The test was failled')

browser.close()