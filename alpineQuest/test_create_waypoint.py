from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from alpineQuest.pages.placemarks_page import PlaceMarks
from alpineQuest.utils.constants import TIMEOUT
from utils.constants import PLACE_MARKS_PAGE

def test_create_waypoint(application):
    # Step 1: Open the app.
    place_mark_page = PlaceMarks(application)
    place_mark_page.open_app()
    # The app is successfully launched.

    # Step 2: Find pleacemark icon
    coordinates = place_mark_page.fined_place_marks_button()

    # Step 3: Click on the pleacemark icon
    place_mark_page.click_button_at_coordinates(coordinates)
    modal_title = place_mark_page.fined_modal_title()
    assert modal_title.text == PLACE_MARKS_PAGE.PLACE_MARKS, f'The title of the modal is not {PLACE_MARKS_PAGE.PLACE_MARKS}'

    # Step 4: Find create a placemark button
    create_place_mark_button = place_mark_page.fined_create_a_place_mark_button()
    create_place_mark_button.click()

    try:
        WebDriverWait(application, TIMEOUT).until(
            EC.presence_of_element_located((AppiumBy.XPATH, PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE_SELECTOR))
        )
    except TimeoutException as ex:
        print("Exception has been thrown: " + str(ex))
    local_modal_title = place_mark_page.fined_local_modal_title()

    assert local_modal_title.text == PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE, f'The title of the modal is not {PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE}'

    # Step 5:  Find and click waypoint button
    waypoint_button = place_mark_page.find_waypoint_button()
    waypoint_button.click()

    waypoint_modal_title = place_mark_page.fined_waypoint_modal_title()
    assert waypoint_modal_title.is_displayed()
    assert waypoint_modal_title.text == PLACE_MARKS_PAGE.WAYPOINT, f'The title of the modal is not {PLACE_MARKS_PAGE.WAYPOINT}'

    # Step 6:  Create waypoint
    input_field = place_mark_page.fined_name_input_selector

