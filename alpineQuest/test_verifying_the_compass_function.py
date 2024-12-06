from alpineQuest.utils.constants import COMPASS_PAGE
from alpineQuest.pages.compass_page import CompassPage
from utils.constants import GPS_PAGE


def test_verify_the_compass_function(application):
    # Step 1: Open the app.
    compass_page = CompassPage(application)
    compass_page.open_app()
    # The app is successfully launched.

    # Step 2: Find Compass icon
    coordinates = compass_page.find_compass_button()

    # Step 3: Click Compass icon
    compass_page.click_button_at_coordinates(coordinates)
    modal_title = compass_page.find_modal_title()

    assert modal_title.text == COMPASS_PAGE.TITLE, f'The title of the modal is not {COMPASS_PAGE.TITLE}'

    # Step 4: Switch on Compass
    compass_switch_on = compass_page.find_switch_compass_button()
    compass_switch_on.click()
    assert compass_switch_on.text != GPS_PAGE.TEXT_OFF, "First switch did not change state or was not clicked."

    # Step 5: Click Compass button and close modal
    compass_page.close_compass_modal()

    # Step 6 Find Compass icon
    coordinates = compass_page.find_green_compass_button()

    # Step 7: Click Compass icon
    compass_page.click_button_at_coordinates(coordinates)
    modal_title = compass_page.find_modal_title()
    assert modal_title.text == COMPASS_PAGE.TITLE, f'The title of the modal is not {COMPASS_PAGE.TITLE}'

    # Step 7: Switch off Compass
    compass_switch_on = compass_page.find_switch_on_compass_button()
    compass_switch_on.click()
    assert compass_switch_on.text == GPS_PAGE.TEXT_OFF, "First switch did not change state or was not clicked."

    # Step 5: Click Compass button and close modal
    compass_page.close_compass_off_modal()

