import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = 'http://suninjuly.github.io/selects1.html'
    path = 'C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(link)
    result = int(driver.find_element(By.ID, 'num1').text) + int(driver.find_element(By.ID, 'num2').text)

    dropdown_list = driver.find_elements(By.CSS_SELECTOR, 'select option')
    dropdown_list_values = []
    del dropdown_list[0]

    for i in range(len(dropdown_list)):
        dropdown_list_values.append(dropdown_list[i].get_attribute('value'))
        dropdown_list_values[i] = int(dropdown_list_values[i])
        if dropdown_list_values[i] == result:
            dropdown = driver.find_element(By.ID, 'dropdown')
            dropdown.click()
            dropdown_list[i].click()
            submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
            submit.click()
            break

finally:
    time.sleep(10)
    driver.quit()
