from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
print(driver.find_element_by_css_selector('td:first-child').text)
driver.find_element_by_xpath('/html/body/table/tbody/tr/th')
print(driver.find_element_by_xpath('//th').text)
driver.find_element_by_xpath('//th[text() = "Month"]')
driver.find_element_by_xpath('//button[@id="clickOnMe"]')
driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table")
list_ele = len(driver.find_elements_by_xpath('//th'))
print(list_ele)
driver.find_element_by_xpath('checkbox').click()




