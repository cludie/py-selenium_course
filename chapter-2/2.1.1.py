import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    link = 'http://suninjuly.github.io/get_attribute.html'
    driver = webdriver.Chrome(path)
    driver.get(link)

    treasure = driver.find_element(By.ID, 'treasure')
    treasurer_value = treasure.get_attribute('valuex')
    result = calc(int(treasure_value))

    input = driver.find_element(By.ID, 'answer')
    input.send_keys(result)

    checkbox = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()

    radio = driver.find_element(By.CSS_SELECTOR, '[value="robots"]')
    radio.click()

    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(3)
    driver.quit()
