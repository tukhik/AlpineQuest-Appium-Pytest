from appium.webdriver.common.appiumby import AppiumBy

from alpineQuest.pages.alpine_quest_page import AlpineQuestPage
from alpineQuest.utils.constants import ALPINE_QUEST_PAGE, APP_ACTIVITY

def test_close_app(application):
    # Step 1: Open the app.
    alpine_quest_page = AlpineQuestPage(application)
    alpine_quest_page.open_app()
    # The app is successfully launched.

    # Step 2: Find Compass icon
    coordinates = alpine_quest_page.find_alpine_button()

    # Step 3: Click Compass icon
    alpine_quest_page.click_compass_button(coordinates)
    modal_title = alpine_quest_page.find_item((AppiumBy.XPATH, ALPINE_QUEST_PAGE.TITLE_SELECTOR))

    assert modal_title.text == ALPINE_QUEST_PAGE.TITLE, f'The title of the modal is not {ALPINE_QUEST_PAGE.TITLE}'

    # Step 4: Click exit button
    exit_button = alpine_quest_page.find_item((AppiumBy.XPATH, ALPINE_QUEST_PAGE.EXIT_BUTTON_SELECTOR))

    assert exit_button.text == ALPINE_QUEST_PAGE.EXIT_BUTTON, f'The title of the modal is not {ALPINE_QUEST_PAGE.EXIT_BUTTON}'

    exit_button.click()
    app_state = application.query_app_state(APP_ACTIVITY)
    assert app_state == 0, f'The app is running'
