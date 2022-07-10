import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/math.html'
    driver = webdriver.Chrome('C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe')

    driver.get(link)
    x = driver.find_element(By.ID, 'input_value')
    y = calc(x.text)

    input = driver.find_element(By.ID, 'answer')
    input.send_keys(y)

    checkbox = driver.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()

    radio = driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()

finally:
    time.sleep(3)
    driver.quit()
