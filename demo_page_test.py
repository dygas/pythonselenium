from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
driver.maximize_window()