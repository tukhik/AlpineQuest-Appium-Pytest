from alpineQuest.pages.base_page import BasePage
from alpineQuest.utils.constants import ALPINE_QUEST_PAGE


class AlpineQuestPage(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def find_alpine_button(self):
        return self.find_button_by_image(ALPINE_QUEST_PAGE.MENU_BUTTON_SELECTOR)

    def click_compass_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)

    def find_item(self, element):
        return self.find(element)
