from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
elements  = driver.find_elements_by_tag_name('papa')
if len(elements)>0:
    print('jest')
else:
    print('nie')
driver.quit()


try:
    driver.find_element_by_tag_name('papa')
    print('rlrment istnieje ')
except NoSuchElementException:
    print('nie istnieje')