from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from alpineQuest.utils.constants import PLACE_MARKS_PAGE

create_place_mark_text_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.CREATE_PLACE_MARK_BUTTON)
waypoint_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.WAYPOINT_TEXT_SELECTOR)
name_input_selector = (AppiumBy.XPATH,  PLACE_MARKS_PAGE.INPUT_SELECTOR)
modal_title = (AppiumBy.XPATH, PLACE_MARKS_PAGE.MODAL_TITLE)
secondary_modal_title = (AppiumBy.XPATH, PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE_SELECTOR)


class PlaceMarks(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def fined_place_marks_button(self):
        return self.find_button_by_image(PLACE_MARKS_PAGE.MENU_BUTTON_SELECTOR)

    def click_please_marks_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)

    def fined_modal_title(self):
        return self.find(modal_title)

    def fined_create_a_place_mark_button(self):
        return self.find(create_place_mark_text_selector)

    def fined_local_modal_title(self):
        return self.find(secondary_modal_title)

    def fined_waypoint_button(self):
        return self.find(PLACE_MARKS_PAGE.WAYPOINT)

    def find_waypoint_button(self):
        return self.find(waypoint_selector)

    def fined_waypoint_modal_title(self):
        return self.find(waypoint_selector)

    def fined_name_input_selector(self):
        return self.find(name_input_selector)

    def wait(self, element):
        return self.wait_element(element)

