import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)

    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x = driver.find_element(By.ID, 'input_value').text
    result = calc(x)

    input = driver.find_element(By.ID, 'answer')
    input.send_keys(result)

    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()


finally:
    time.sleep(10)
    driver.quit()
