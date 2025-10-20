from pages.stellar_burger_layout_page import StellarBurgerPage
from locators import OrderFeedLocators

class OrderFeedPage(StellarBurgerPage):

    def get_orders_count_total(self):
        return self.wait_visibility_of_element(OrderFeedLocators.ORDER_FEED_NUM_TOTAL).text
        
    def get_orders_count_today(self):
        return self.wait_visibility_of_element(OrderFeedLocators.ORDER_FEED_NUM_TODAY).text

    def get_list_orders_in_work(self):
        return self.wait_visibility_of_element(OrderFeedLocators.LIST_ORDERS_IN_WORK).text

    