from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

#WebDriver Setup
driver = webdriver.Chrome('C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\pe4enka_farm\\chromedriver.exe')
driver.set_window_size('1900', '1000')
options = Options()
useragent = UserAgent()
userAgent = useragent.random
options.add_argument(f'user-agent={userAgent}')