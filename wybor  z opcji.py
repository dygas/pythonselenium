from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
auto_select = Select(driver.find_element_by_tag_name('select'))
auto_select.select_by_visible_text('Volvo')
auto_select.select_by_value('saab')
auto_select.select_by_index(0)

