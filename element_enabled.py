from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
first_name_input = driver.find_element_by_name('fname')
driver.save_screenshot('screenshots2/przed.png')
if first_name_input.is_enabled():
    first_name_input.send_keys('element dostepny')
else:
    print('element nie jest dostępny')

driver.save_screenshot('screenshots2/po.png')
driver.quit()
