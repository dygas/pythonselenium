import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('file:///Users/grzegorzdygas/Desktop/test.html')
    driver.maximize_window()
    yield
    driver.quit()
def test_method(test_setup):
    assert driver.title == 'Strona testowa'

def test_method2(test_setup):
    assert driver.title == 'Strona testowa'