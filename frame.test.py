from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/iFrameTest.html')

print(driver.find_element_by_tag_name('h1').text)
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
print(driver.find_element_by_tag_name('h1').text)
driver.switch_to.default_content()
driver.quit()