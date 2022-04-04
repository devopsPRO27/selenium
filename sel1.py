import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\\Users\\hothaifa\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
time.sleep(3)
driver.find_element(by=By.XPATH,value='//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
time.sleep(4)
driver.find_element(by=By.ID,value='email_create').send_keys('hoth@a2.a2')
driver.find_element(by=By.ID,value='SubmitCreate').click()
time.sleep(10)
driver.find_element(by=By.XPATH,value='//*[@id="id_gender2"]').click()
driver.find_element(by=By.NAME,value='customer_firstname').send_keys('hothaifa')
driver.find_element(by=By.ID,value='customer_lastname').send_keys('zoubi')
driver.find_element(by=By.NAME,value='passwd').send_keys('12345')
#input to last name textbox
driver.find_element(by=By.XPATH,value='//*[@id="days"]/option[16]').click()
driver.find_element(by=By.XPATH,value='//*[@id="months"]/option[4]').click()
driver.find_element(by=By.XPATH,value='//*[@id="years"]/option[29]').click()
driver.find_element(by=By.NAME,value='newsletter').click()

driver.find_element(by=By.ID,value='company').send_keys('Hodicode')
driver.find_element(by=By.NAME,value='address1').send_keys("23,wallstreet")
driver.find_element(by=By.NAME,value='city').send_keys('NEW YORK')
driver.find_element(by=By.XPATH,value='//*[@id="postcode"]').send_keys('18950')
driver.find_element(by=By.NAME,value='phone_mobile').send_keys('0526618010')


