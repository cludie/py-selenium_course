import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'https://vk.com/edwardspicybrain'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.set_window_size('1900', '1000')
    driver.get(link)

    driver.find_element(By.ID, 'post685585335_12').screenshot('only_one.png')

finally:
    time.sleep(3)
    driver.quit()