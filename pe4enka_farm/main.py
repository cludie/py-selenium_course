from accounts import login, password, acc_counter
from driver import driver
from selenium.webdriver.common.by import By
import time

for i in range(acc_counter):
    driver.get('https://vk.com')
    driver.find_element(By.CSS_SELECTOR, '.VkIdForm__signInButton').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'login').send_keys(login[i])
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(password[i])
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(100)

