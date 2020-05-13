from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://demos.telerik.com/kendo-ui/dragdrop/index')
xxx = driver.find_element_by_id('draggable')
yyy = driver.find_element_by_id('droptarget')
webdriver.ActionChains(driver).drag_and_drop(xxx,yyy).perform()

