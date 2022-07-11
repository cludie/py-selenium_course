import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, '.trollface').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID, 'answer').send_keys(calc(driver.find_element(By.ID, 'input_value').text))
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(10)
    driver.quit()