import time
from selenium import webdriver

# Main Page

driver = webdriver.Chrome(/builds/ws/RedWebappCheck/chromedriver) 
driver.get('https://cat.deploymbed.com/main#/');
driver.fullscreen_window()
time.sleep(5)
driver.save_screenshot('main.png')

# Floor Page

driver.find_element_by_xpath("//*[@id='5b2bd35272782e62cded0465']").click()
driver.find_element_by_xpath("//*[@id='selFloor']/option[1]").click()
time.sleep(5)
driver.save_screenshot('floor.png')

# Admin Page

link = driver.find_element_by_xpath("//*[@id='settings']")
print (link)
#link.click()
time.sleep(5)

driver.quit()


