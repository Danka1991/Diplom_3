from pages.stellar_burger_layout_page import StellarBurgerPage
from locators import AuthLocators
from curl import Urls

class LoginPage(StellarBurgerPage):

    def sign_in(self, email, password):
        self.click_personal_acc_btn()
        self.page_url_contains(Urls.login_url)
        self.wait_visibility_of_element(AuthLocators.EMAIL_INPUT)
        self.send_keys_to_input(AuthLocators.EMAIL_INPUT, email)
        self.send_keys_to_input(AuthLocators.PASS_INPUT, password)
        return self.click_on_element(AuthLocators.LOGIN_BTN)

    