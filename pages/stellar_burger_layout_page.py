from pages.base_page import BasePage
from locators import CommonLocators
import allure 

class StellarBurgerPage(BasePage):
    
    @allure.step('Нажимаем на «Конструктор»')
    def click_on_constructor_btn(self):
        return self.click_on_element(CommonLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step('Нажимаем на «Лента заказов»')
    def click_on_order_feed_btn(self):
        return self.click_on_element(CommonLocators.ORDER_FEED)
    
    @allure.step('Нажимаем на «Личный Кабинет»')
    def click_personal_acc_btn(self):
        return self.click_on_element(CommonLocators.PERSONAL_ACCOUNT_BUTTON)