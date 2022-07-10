import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link =
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)


finally:
    time.sleep(10)
    driver.quit()