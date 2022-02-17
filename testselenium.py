from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com.br")  
campodebusca = driver.find_element(by="name",value="q")
campodebusca.send_keys("nextmuv")
campodebusca.send_keys(Keys.RETURN)              

time.sleep(5)
driver.close()