import time
from selenium import webdriver

# Main Page

driver = webdriver.Chrome() 
driver.get('https://cat.deploymbed.com/main#/');
driver.fullscreen_window()
time.sleep(5)

driver.quit()


