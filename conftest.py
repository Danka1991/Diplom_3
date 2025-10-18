import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
import pytest
from curl import Urls
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=[
    'firefox', 
    'chrome'
    ])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        chrome_binary = r'd:\chrome-win64\chrome.exe'
        options = Options()
        options.binary_location = chrome_binary
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    driver.get(Urls.main_url)
    yield driver
    driver.quit()