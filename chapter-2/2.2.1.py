import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)
    driver.find_element(By.ID, 'answer').send_keys(calc(int(driver.find_element(By.ID, 'input_value').text)))
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = driver.find_element(By.ID, 'robotsRule')
    driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    driver.quit()