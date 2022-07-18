import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
#"Congratulations! You have successfully registered!"

class test_Registration(unittest.TestCase):
    def test_registration1(self):
        driver = webdriver.Chrome('C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe')
        driver.get('http://suninjuly.github.io/registration1.html')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
        self.assertEqual('Congratulations! You have successfully registered!',
                         driver.find_element(By.CSS_SELECTOR, 'h1').text
                         , "Wrong welcome text!")

    def test_registration2(self):
        driver = webdriver.Chrome('C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe')
        driver.get('http://suninjuly.github.io/registration2.html')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys('123')
        driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
        self.assertEqual('Congratulations! You have successfully registered!',
                         driver.find_element(By.CSS_SELECTOR, 'h1').text
                         , "Wrong welcome text!")

if __name__ == "__main__":
    unittest.main()