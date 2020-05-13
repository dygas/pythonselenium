from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.execute_script('arguments[0].click();',driver.find_element_by_id('newPage'))
wartosc = 'grzegorz'
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element_by_id('fname'))
#javastript na gorze


driver.quit()




