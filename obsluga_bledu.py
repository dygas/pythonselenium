from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.maximize_window()
driver.find_element_by_id('clickOnMe').click()
driver.switch_to.alert.accept()
driver.find_element_by_id('clickOnMe').click()
driver.switch_to.alert.dismiss()# nie wywoluje alertow ale zostaly pozamykane
