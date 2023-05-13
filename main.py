from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://wikipedia.org')
driver.find_element(By.NAME, "search").send_keys("Python", Keys.ENTER)
#driver.find_element(By.LINK_TEXT, "ABC (programovací jazyk)")

time.sleep(20)