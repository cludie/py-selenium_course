from selenium import webdriver
browser = webdriver.Chrome('C:\\Users\\cludie\\PycharmProjects\\stepik_py-selenium\\drivers\\chromedriver.exe')
browser.execute_script("alert('Your parrot are dead');")