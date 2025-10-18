from selenium.webdriver.common.by import By

class CommonLocators:
    
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    
    ORDER_FEED = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")

class MainPageLocators:

    MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]")

    FLUR_BUN = (By.XPATH, "(//a/p[contains(@class, 'BurgerIngredient_ingredient')])[1]")

    LUM_FILLET_TETRA = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[10]")
    
    INGR_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__')]")

    FIRST_SAUCE = (By.XPATH, "(//div[contains(@class, 'BurgerIngredient_ingredient')])[3]")

    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    BASKET = (By.XPATH, "(//section[contains(@class, 'BurgerConstructor_basket__')])")

    MAKE_ORDER_BTN = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__container__')]/button[text()='Оформить заказ']")

    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__')]")

    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]/div[contains(@class, 'Modal_modal_overlay__')]")
    
    MODAL_OVERLAY_2 = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]/div[contains(@class, 'Modal_modal_overlay__')]")

class OrderFeedLocators:

    ORDER_FEED_NUM_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    ORDER_FEED_NUM_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    LIST_ORDERS_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]")
    
class AuthLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    PASS_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")