import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)

    button = driver.find_element(By.ID, 'book')
    WebDriverWait(driver, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()

    result = calc(driver.find_element(By.ID, 'input_value').text)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'solve').click()




finally:
    time.sleep(10)
    driver.quit()