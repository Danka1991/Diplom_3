from curl import Urls
import allure
from pages.stellar_burger_layout_page import StellarBurgerPage
from pages.main_page import MainPage

class TestBasicFunctionality:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_check_transition_by_constructor_btn(self, driver):
        with allure.step("Перейти в ленту заказов"):   
            stellar_page = StellarBurgerPage(driver)
            stellar_page.click_on_order_feed_btn()
        with allure.step("Вернуться в конструктор через кнопку"):
            stellar_page.click_on_constructor_btn()
        with allure.step("Проверить переход на главную страницу"):    
            assert stellar_page.get_current_url() == Urls.main_url 

    @allure.title('Проверка перехода по клику на раздел «Лента заказов»')
    def test_check_transition_by_the_Order_Feed_section(self, driver):
        with allure.step("Нажать на раздел 'Лента заказов'"):
            stellar_page = StellarBurgerPage(driver)
            stellar_page.click_on_order_feed_btn() 
        with allure.step("Проверить переход на страницу ленты заказов"):     
            assert stellar_page.get_current_url() == Urls.order_feed_url 
        
    @allure.title('Проверка появлнеия всплывающего окна с деталями по клику на ингредиент')
    def test_check_click_on_ingredient(self, driver):
        with allure.step("Кликнуть на ингредиент 'Флюоресцентная булка'"):    
            main_page = MainPage(driver)
            clicked_el = main_page.click_on_flur_bun()
            ingredient_name = clicked_el.text
        with allure.step("Проверить отображение модального окна и наличие названия ингредиента в модальном окне"):   
           assert main_page.is_ingridient_modal_visible() and ingredient_name in main_page.get_text_in_modal()

    @allure.title('Проверка закрытия модального окна по клику на крестик')
    def test_ingredient_modal_close(self, driver):
        with allure.step("Открыть модальное окно ингредиента"):    
            main_page = MainPage(driver)
            main_page.click_on_flur_bun()
            main_page.wait_till_modal_get_visible() 
        with allure.step("Закрыть модальное окно крестиком"):    
            main_page.close_modal()
        with allure.step("Проверить, что модальное окно закрылось"):    
            assert main_page.is_ingridient_modal_visible() == False

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increase(self, driver):
        with allure.step("Получить начальное значение счетчика ингредиента"):
            main_page = MainPage(driver)
            ingredient_count = main_page.get_lum_fillet_tetra_count()
        with allure.step("Добавить ингредиент в заказ"):    
            main_page.add_lum_fillet_tetra_to_order()
        with allure.step("Получить обновленное значение счетчика"):   
            ingredient_count_again = main_page.get_lum_fillet_tetra_count()
        with allure.step("Проверить увеличение счетчика"):    
            assert int(ingredient_count) < int(ingredient_count_again)