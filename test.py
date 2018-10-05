import time
from selenium import webdriver

# Main Page

driver = webdriver.Chrome('/builds/ws/RedWebappCheck/chromedriver') 
driver.get('https://cat.deploymbed.com/main#/');
#driver.fullscreen_window()

time.sleep(5)
driver.save_screenshot('main.png')
driver.quit()


