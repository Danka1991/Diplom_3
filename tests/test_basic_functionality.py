from curl import Urls
import allure
from pages.stellar_burger_layout_page import StellarBurgerPage
from pages.main_page import MainPage

class TestBasicFunctionality:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_check_transition_by_constructor_btn(self, driver):
        stellar_page = StellarBurgerPage(driver)
        stellar_page.click_on_order_feed_btn()
        stellar_page.click_on_constructor_btn()
        assert stellar_page.get_current_url() == Urls.main_url 

    @allure.title('Проверка перехода по клику на раздел «Лента заказов»')
    def test_check_transition_by_the_Order_Feed_section(self, driver):
        stellar_page = StellarBurgerPage(driver)
        stellar_page.click_on_order_feed_btn() 
        assert stellar_page.get_current_url() == Urls.order_feed_url 
        
    @allure.title('Проверка появлнеия всплывающего окна с деталями по клику на ингредиент')
    def test_check_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        clicked_el = main_page.click_on_flur_bun()
        ingredient_name = clicked_el.text
        assert main_page.is_ingridient_modal_visible() and ingredient_name in main_page.get_text_in_modal()

    @allure.title('Проверка закрытия модального окна по клику на крестик')
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_flur_bun()
        main_page.wait_till_modal_get_visible() 
        main_page.close_modal()
        assert main_page.is_ingridient_modal_visible() == False

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        ingredient_count = main_page.get_lum_fillet_tetra_count()
        main_page.add_lum_fillet_tetra_to_order()
        ingredient_count_again = main_page.get_lum_fillet_tetra_count()
        assert int(ingredient_count) < int(ingredient_count_again)