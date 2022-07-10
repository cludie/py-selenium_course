import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = 'http://suninjuly.github.io/find_link_text'
    driver = webdriver.Chrome('C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe')
    driver.get(link)
    time.sleep(1)

    button = driver.find_element(By.LINK_TEXT, link_text)
    button.click()

    input1 = driver.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    driver.quit()