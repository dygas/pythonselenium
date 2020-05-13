from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.w3schools.com')
tutorials_element = driver.find_element_by_id('navbtn_tutorials')
webdriver.ActionChains(driver).move_to_element(tutorials_element).click(tutorials_element).perform()