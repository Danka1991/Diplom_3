import allure

class TestOrderFeed:
    @allure.title("Увеличение счетчика 'Выполнено за всё время' при новом заказе")
    def test_total_orders_counter_increase(self, order):
        with allure.step("Получить значения счетчиков 'Выполнено за всё время'"):    
            orders_count_total = order["orders_count_total"]
            orders_count_total_new = order["orders_count_total_new"]

        with allure.step("Проверить увеличение счетчика 'Выполнено за всё время'"):   
            assert int(orders_count_total) < int(orders_count_total_new)

    @allure.title("Увеличение счетчика 'Выполнено за всё сегодня' при новом заказе")
    def test_today_orders_counter_increase(self, order):
        with allure.step("Получить значения счетчиков 'Выполнено за сегодня'"):    
            orders_count_today = order["orders_count_today"]
            orders_count_today_new = order["orders_count_today_new"]
            
        with allure.step("Проверить увеличение счетчика 'Выполнено за сегодня'"):    
            assert int(orders_count_today) < int(orders_count_today_new)

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_in_work_list(self, order):
        with allure.step("Получить номер созданного заказа"):    
            order_id = order["order_id"]
            list_orders_in_work = order["list_orders_in_work"]
            
        with allure.step("Получить список заказов в работе"):    
            assert order_id in list_orders_in_work  # новый заказ сперва попадает в список Готовы: 
                                                    # потом через некоторое время он переносится из списка Готовы: в список В работе: 
                                                    # после перезагрузки заказ уже окончательно в списке Готовы: 
                                                    # я считаю что это баг
        
        
