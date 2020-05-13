from selenium import webdriver
from selenium.webdriver.common.by import By# do pliku By Id
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.maximize_window()
driver.find_element_by_id('fname')
driver.find_element(By.ID,'fname')
driver.find_element_by_name('fname')
driver.find_element_by_link_text('Visit W3Schools.com!')
driver.find_element_by_partial_link_text('W3Schools')
driver.find_element_by_class_name('topSecret')
driver.find_element_by_tag_name('a')
driver.find_element_by_tag_name('label')
driver.find_element_by_tag_name('p')



driver.find_elements_by_css_selector('a')
driver.find_elements_by_css_selector('img#smileImage')
driver.find_elements_by_css_selector('p.topSecret')
print(driver.find_element_by_css_selector('th:first-child').text)
print(driver.find_element_by_css_selector('th:last-child').text)





driver.quit()



