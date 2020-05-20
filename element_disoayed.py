from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')


paragraph = driver.find_element_by_tag_name('p')
if paragraph.is_displayed():
    print('is displayed')
    print(paragraph.text)
else:
    print('not displayed')
    paragraph.get_attribute("textContent")

driver.quit()
