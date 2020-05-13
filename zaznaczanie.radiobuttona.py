from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.find_element_by_name('gender').click()
print(driver.find_element_by_tag_name('h1').text)
print(driver.find_element_by_tag_name('p').get_attribute('textContent'))