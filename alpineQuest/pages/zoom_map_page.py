from alpineQuest.pages.base_page import BasePage
from alpineQuest.utils.constants import ZOOM_MAP_PAGE



class ZoomMapPage(BasePage):
    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def fined_plus_button(self):
        return self.find_button_by_image(ZOOM_MAP_PAGE.PLUS_BUTTON_SELECTOR)

    def click_plus_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)

    def fined_minus_button(self):
        return self.find_button_by_image(ZOOM_MAP_PAGE.MINUS_BUTTON_SELECTOR)

    def click_minus_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)
