from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')

checkbox = driver.find_element_by_xpath('//input[@type = "checkbox"]')
checkbox.click()
if checkbox.is_selected():
    print('jest')
driver.quit()