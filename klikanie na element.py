from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.maximize_window()
#1
driver.find_element_by_id('clickOnMe').click()
#2
#click_me_button = driver.find_element_by_id('clickOnMe')
#click_me_button.click()