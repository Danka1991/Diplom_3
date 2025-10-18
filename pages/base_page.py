import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver   

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание загрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
      
    @allure.step('Ожидание скрытия элемента')
    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))
    
    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.scroll_to_element(locator)
        el = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        el.click()
        return el

    @allure.step('Вводим значения')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)    

    @allure.step('Текст элемента')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text
    
    @allure.step('Возвращаем URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переходим на другую вкладку')
    def switch_to_next_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ищем совпадение в URL с нашей подстракой')
    def page_url_contains(self, str):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(str))
    
    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        elements = self.driver.find_elements(*locator)
        if not elements:
            return False
        return elements[0].is_displayed()
    
    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)