import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
import allure
import pytest
from curl import Urls
from selenium.webdriver.chrome.options import Options
from data import Credentials
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@pytest.fixture(params=[
    'firefox', 
    'chrome'
    ])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        chrome_binary = os.environ["CHROME_BIN"]
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

@pytest.fixture()
@allure.step("Aвторизация пользователя")
def driver_with_authorized_user(driver):
    with allure.step(f"Авторизация пользователя {Credentials.email}"):
        login_page = LoginPage(driver)   
        login_page.sign_in(Credentials.email, Credentials.password)
    return driver

@pytest.fixture()
@allure.step("Создание заказа авторизованным пользователем")
def order(driver_with_authorized_user):
    with allure.step("Авторизоваться и создать заказ"): 
        result = {}
        main_page = MainPage(driver_with_authorized_user)  
        order_feed_page = OrderFeedPage(driver_with_authorized_user)
        main_page.wait_till_overlay_get_invisible()
    with allure.step("Переход в ленту заказов"):    
        main_page.click_on_order_feed_btn()
        main_page.page_url_contains(Urls.order_feed_url)
    with allure.step("Сбор исходных данных о заказах"):    
        result["orders_count_total"] = order_feed_page.get_orders_count_total() 
        result["orders_count_today"] = order_feed_page.get_orders_count_today() 
    with allure.step("Создание заказа"):    
        order_feed_page.click_on_constructor_btn()
        main_page.add_simple_burger_to_busket()
        main_page.click_make_order()
        main_page.wait_till_overlay_get_invisible()
        result["order_id"] = main_page.get_order_id()
        main_page.close_modal()
        main_page.wait_till_overlay_get_invisible()
        main_page.wait_till_overlay_2_get_invisible()
    with allure.step("Проверка обновленных данных"):    
        main_page.click_on_order_feed_btn()
        main_page.page_url_contains(Urls.order_feed_url)
        result["orders_count_total_new"] = order_feed_page.get_orders_count_total()   
        result["orders_count_today_new"] = order_feed_page.get_orders_count_today()   
        result["list_orders_in_work"] = order_feed_page.get_list_orders_in_work()     
        return result 