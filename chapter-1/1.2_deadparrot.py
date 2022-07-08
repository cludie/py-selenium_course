import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.set_window_size('1900', '1000')
driver.get('https://vk.com/edwardspicybrain')
time.sleep(1)
deadparrot_picture = driver.find_element(By.CSS_SELECTOR, '.page_post_thumb_wrap')
deadparrot_picture.click()
time.sleep(0.2)
unauth = driver.find_element(By.CSS_SELECTOR, '.UnauthActionBox__close')
unauth.click()







