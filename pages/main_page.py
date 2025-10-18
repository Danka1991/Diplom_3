from locators import MainPageLocators
from pages.stellar_burger_layout_page import StellarBurgerPage

class MainPage(StellarBurgerPage):
    
    def click_on_flur_bun(self):
        return self.click_on_element(MainPageLocators.FLUR_BUN)
    
    def click_make_order(self):
        return self.click_on_element(MainPageLocators.MAKE_ORDER_BTN)
    
    def get_text_in_modal(self):
        return self.get_text_on_element(MainPageLocators.MODAL)
    
    def is_ingridient_modal_visible(self):
        return self.check_displaying_of_element(MainPageLocators.MODAL)
    
    def wait_till_modal_get_visible(self):
        return self.wait_visibility_of_element(MainPageLocators.MODAL)
    
    def wait_till_overlay_get_invisible(self):
        return self.wait_invisibility_of_element(MainPageLocators.MODAL_OVERLAY) 
            
    def wait_till_overlay_2_get_invisible(self):
        return self.wait_invisibility_of_element(MainPageLocators.MODAL_OVERLAY_2) 
    
    def close_modal(self):
        return self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    def get_order_id(self):
        return self.wait_visibility_of_element(MainPageLocators.ORDER_ID).text
    
    def get_lum_fillet_tetra_count(self):
        self.scroll_to_element(MainPageLocators.LUM_FILLET_TETRA)
        return self.wait_visibility_of_element(MainPageLocators.LUM_FILLET_TETRA).find_element(*MainPageLocators.INGR_COUNTER).text

    def add_lum_fillet_tetra_to_order(self):
        return self.drag_and_drop_element(self.wait_visibility_of_element(MainPageLocators.LUM_FILLET_TETRA), self.wait_visibility_of_element(MainPageLocators.BASKET))
    
    def add_flur_bun_to_order(self):
        return self.drag_and_drop_element(self.wait_visibility_of_element(MainPageLocators.FLUR_BUN), self.wait_visibility_of_element(MainPageLocators.BASKET))

    def add_first_sause_to_order(self):
        return self.drag_and_drop_element(self.wait_visibility_of_element(MainPageLocators.FIRST_SAUCE), self.wait_visibility_of_element(MainPageLocators.BASKET))

    def add_simple_burger_to_busket(self):
        self.add_flur_bun_to_order()
        self.add_lum_fillet_tetra_to_order()
        self.add_first_sause_to_order()
        return True