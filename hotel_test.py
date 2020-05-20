from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://www.kurs-selenium.pl/demo/')
driver.find_element_by_xpath("//span[text() ='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//span[text()='Dubai']").click()