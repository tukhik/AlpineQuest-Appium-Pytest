from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from alpineQuest.utils.constants import COMPASS_PAGE

switch_off_selector = (AppiumBy.XPATH, COMPASS_PAGE.SWITCH_OFF)
switch_on_selector = (AppiumBy.XPATH, COMPASS_PAGE.SWITCH_ON)
modal_title = (AppiumBy.XPATH, COMPASS_PAGE.MODAL_TITLE_SELECTOR)


class CompassPage(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def find_compass_button(self):
        return self.find_button_by_image(COMPASS_PAGE.COMPASS_BUTTON_SELECTOR)

    def click_compass_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)

    def find_modal_title(self):
        return self.find(modal_title)

    def find_switch_compass_button(self):
        return self.find(switch_off_selector)

    def close_compass_modal(self):
        coordinates = self.find_button_by_image(COMPASS_PAGE.CLOSE_MODAL_ICON)
        return self.click_button_at_coordinates(coordinates)

    def find_green_compass_button(self):
        coordinates = self.find_button_by_image(COMPASS_PAGE.GREEN_COMPASS)
        return self.click_button_at_coordinates(coordinates)

    def find_switch_on_compass_button(self):
        return self.find(switch_on_selector)

    def close_compass_off_modal(self):
        coordinates = self.find_button_by_image(COMPASS_PAGE.COMPASS_OFF)
        return self.click_button_at_coordinates(coordinates)
