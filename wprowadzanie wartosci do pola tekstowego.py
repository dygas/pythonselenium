from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.find_element_by_id('fname').send_keys('bartek')
driver.find_element_by_name('password').send_keys(Keys.ENTER)