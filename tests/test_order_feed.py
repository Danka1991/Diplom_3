import allure
from helper import sign_in, make_order

class TestOrderFeed:
    @allure.title("Увеличение счетчика 'Выполнено за всё время' при новом заказе")
    def test_total_orders_counter_increase(self, driver):
        driver = sign_in(driver)
        order = make_order(driver)
        orders_count_total = order["orders_count_total"]
        orders_count_total_new = order["orders_count_total_new"]

        assert int(orders_count_total) < int(orders_count_total_new)

    @allure.title("Увеличение счетчика 'Выполнено за всё сегодня' при новом заказе")
    def test_today_orders_counter_increase(self, driver):
        driver = sign_in(driver)
        order = make_order(driver)
        orders_count_today = order["orders_count_today"]
        orders_count_today_new = order["orders_count_today_new"]
        
        assert int(orders_count_today) < int(orders_count_today_new)

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_in_work_list(self, driver):
        driver = sign_in(driver)
        order = make_order(driver)
        order_id = order["order_id"]
        list_orders_in_work = order["list_orders_in_work"]
        
        assert order_id in list_orders_in_work  # новый заказ сперва попадает в список Готовы: 
                                                # потом через некоторое время он переносится из списка Готовы: в список В работе: 
                                                # после перезагрузки заказ уже окончательно в списке Готовы: 
                                                # я считаю что это баг
        
        
