#25.271567889970747
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome('C:\chromedriver.exe')
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    time.sleep(1)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(3)
    browser.quit()