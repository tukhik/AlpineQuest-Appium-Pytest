from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from alpineQuest.utils.constants import PLACE_MARKS_PAGE

create_place_mark_text_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.CREATE_PLACE_MARK_BUTTON)
find_search_location_button_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.SEARCH_LOCATION_BUTTON)
waypoint_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.WAYPOINT_TEXT_SELECTOR)
name_input_selector = (AppiumBy.CLASS_NAME,  PLACE_MARKS_PAGE.INPUT_SELECTOR)
modal_title = (AppiumBy.XPATH, PLACE_MARKS_PAGE.MODAL_TITLE)
secondary_modal_title = (AppiumBy.XPATH, PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE_SELECTOR)
ok_button = (AppiumBy.XPATH, PLACE_MARKS_PAGE.OK_BUTTON_SELECTOR)
displayed_place_mark_text_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.DISPLAYED_PLACE_MARKS_BUTTON)
created_waypoint = (AppiumBy.XPATH, PLACE_MARKS_PAGE.CRATED_WAYPOINT)
close_modal =(AppiumBy.XPATH, PLACE_MARKS_PAGE.CLOSE_MODAL_ICON)
rout_button_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.ROUT_BUTTON_SELECTOR)
lock_icon_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.LOCK_ICON)
cancel_button = (AppiumBy.XPATH, PLACE_MARKS_PAGE.CANCEL_BUTTON_SELECTOR)
search_a_location_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.SEARCH_A_LOCATION)
search_by_name_selector = (AppiumBy.XPATH, PLACE_MARKS_PAGE.SEARCH_BY_NAME_SELECTOR)
location_input = (AppiumBy.CLASS_NAME,  PLACE_MARKS_PAGE.LOCATION_INPUT_SELECTOR)
search_button =  (AppiumBy.CLASS_NAME,  PLACE_MARKS_PAGE.SEARCH_BUTTON_SELECTOR)
searched_information_title =  (AppiumBy.CLASS_NAME,  PLACE_MARKS_PAGE.SEARCHED_INFORMATION_SELECTOR)
display_all = (AppiumBy.CLASS_NAME,  PLACE_MARKS_PAGE.DISPLAY_ALL_BUTTON)


class PlaceMarks(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def find_place_marks_button(self):
        return self.find_button_by_image(PLACE_MARKS_PAGE.MENU_BUTTON_SELECTOR)

    def click_please_marks_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)

    def find_modal_title(self):
        return self.find(modal_title)

    def find_create_a_place_mark_button(self):
        return self.find(create_place_mark_text_selector)

    def find_search_location_button(self):
        return self.find(find_search_location_button_selector)

    def find_local_modal_title(self):
        return self.find(secondary_modal_title)

    def find_waypoint_button(self):
        return self.find(waypoint_selector)

    def find_waypoint_modal_title(self):
        return self.find(waypoint_selector)

    def find_name_input_selector(self):
        return self.find(name_input_selector)

    def wait_for_visible_element(self, element):
        return self.wait_element(element)

    def find_ok_button(self):
        return self.find(ok_button)

    def write_waypoint_name(self, input_field, text):
        return self.write_text_in_input(input_field, text)

    def find_displayed_place_marks(self):
        return self.find(displayed_place_mark_text_selector)

    def find_created_waypoint(self):
        return self.find(created_waypoint)

    def find_close_modal_icon(self):
        return self.find(close_modal)

    def find_rout_button(self):
        return self.find(rout_button_selector)

    def find_lock_icon(self):
        return self.find(lock_icon_selector)

    def cancel_button(self):
        return self.find(cancel_button)

    def waite_until_modal_closed(self, element):
        return self.wait_element_is_not_visible(element)

    def find_search_by_name_button(self):
        return self.find(search_by_name_selector)

    def find_search_location_input(self):
        return self.find(location_input)

    def write_search_location_name(self, input_field, text):
        return self.write_text_in_input(input_field, text)

    def find_search_button(self):
        return self.find(search_button)

    def find_searched_information_title(self):
        return self.find(searched_information_title)

    def find_display_all_button(self):
        return self.find(display_all)

    def find_by_xpath(self, xpath):
        return self.find((AppiumBy.XPATH, xpath))

    def long_press_button(self, button_selector):
        return self.long_press(button_selector)
