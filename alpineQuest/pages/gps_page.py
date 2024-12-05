from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from alpineQuest.utils.constants import GPS_PAGE

switch_off_selector = (AppiumBy.XPATH, GPS_PAGE.SWITCH_OFF)
switch_on_selector = (AppiumBy.XPATH, GPS_PAGE.SWITCH_ON)
modal_title = (AppiumBy.XPATH, GPS_PAGE.MODAL_TITLE)

class PositioningPage(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()
    
    def click_gps_button(self):
        return self.find_and_click_button_by_image(GPS_PAGE.MENU_BUTTON_SELECTOR)

    def fined_modal_title(self):
        return self.find(modal_title)
    
    def fined_switch_location_button(self):
        return self.find(switch_off_selector)

    
    def fined_and_click_location_gps_on_button(self):
        return self.find(switch_on_selector)
    
    def close_gps_modal(self):
        return self.find_and_click_button_by_image(GPS_PAGE.CLOSE_MODAL_ICON)

    