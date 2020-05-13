from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.find_element_by_id('smileImage').size.get('height')
print(driver.find_element_by_id('smileImage').size.get('height'))
print(driver.find_element_by_id('smileImage').get_attribute('naturalHeight'))