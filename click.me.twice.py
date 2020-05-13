from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/double.click.html')


button = driver.find_element_by_id('bottom')
webdriver.ActionChains(driver).double_click(button).perform()