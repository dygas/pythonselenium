from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
username_input = driver.find_element_by_name('username')
username_input.clear()
driver.find_element_by_name('username').send_keys('pomuryadam')
