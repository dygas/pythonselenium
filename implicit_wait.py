from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver,10,0.5)
driver.get('file:///Users/grzegorzdygas/Downloads/original%20(4).html')
driver.find_element_by_id('clickOnMe').click()
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'p')))
print(driver.find_element_by_tag_name('p').text)

