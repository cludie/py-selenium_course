import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/file_input.html'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)
    forms = driver.find_elements(By.CSS_SELECTOR, '.form-control')
    for form in forms:
        form.send_keys('123')
    file_input = driver.find_element(By.ID, 'file')
    ##Отправляем файл (не особо понял, как и что)
    directory = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\chapter-2\\'
    file_name = "2.2.3_input_file.txt"
    file_path = os.path.join(directory, file_name)
    file_input.send_keys(file_path)

    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()


finally:
    time.sleep(3)
    driver.quit()