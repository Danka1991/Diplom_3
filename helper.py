from data import Credentials
from locators import AuthLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from curl import Urls
from pages.stellar_burger_layout_page import StellarBurgerPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

def sign_in(driver):
    # Проходим авторизацию
    stellar_page = StellarBurgerPage(driver)
    stellar_page.click_personal_acc_btn()
    stellar_page.page_url_contains(Urls.login_url)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthLocators.EMAIL_INPUT))       
    stellar_page.send_keys_to_input(AuthLocators.EMAIL_INPUT, Credentials.email)
    stellar_page.send_keys_to_input(AuthLocators.PASS_INPUT, Credentials.password)
    stellar_page.click_on_element(AuthLocators.LOGIN_BTN)
    return driver

def make_order(driver):
    result = {}
    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)
    main_page.wait_till_overlay_get_invisible()
    main_page.click_on_order_feed_btn()
    main_page.page_url_contains(Urls.order_feed_url)
    result["orders_count_total"] = order_feed_page.get_orders_count_total() # orders_count_total = сохраняем значение колва заказов всего
    result["orders_count_today"] = order_feed_page.get_orders_count_today() # orders_count_today = сохраняем значение колва заказов сегодня
    order_feed_page.click_on_constructor_btn()
    main_page.add_simple_burger_to_busket()
    main_page.click_make_order()
    main_page.wait_till_overlay_get_invisible()
    result["order_id"] = main_page.get_order_id()
    main_page.close_modal()
    main_page.wait_till_overlay_get_invisible()
    main_page.wait_till_overlay_2_get_invisible()
    main_page.click_on_order_feed_btn()
    main_page.page_url_contains(Urls.order_feed_url)
    result["orders_count_total_new"] = order_feed_page.get_orders_count_total()   # orders_count_total_new = извлекаем текст колва заказов всего
    result["orders_count_today_new"] = order_feed_page.get_orders_count_today()   # orders_count_today_new = извлекаем текст колва заказов сегодня
    result["list_orders_in_work"] = order_feed_page.get_list_orders_in_work()     # list_orders_in_work = извлекаем текст номеров заказов в работе LIST_ORDERS_IN_WORK
    return result