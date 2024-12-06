from time import sleep

from alpineQuest.pages.placemarks_page import PlaceMarks
from utils.constants import PLACE_MARKS_PAGE

def test_create_waypoint(application):
    # Step 1: Open the app.
    place_mark_page = PlaceMarks(application)
    place_mark_page.open_app()
    # The app is successfully launched.

    # Step 2: Find pleacemark icon
    coordinates = place_mark_page.find_place_marks_button()

    # Step 3: Click on the pleacemark icon
    place_mark_page.click_button_at_coordinates(coordinates)
    modal_title = place_mark_page.find_modal_title()
    assert modal_title.text == PLACE_MARKS_PAGE.PLACE_MARKS, f'The title of the modal is not {PLACE_MARKS_PAGE.PLACE_MARKS}'

    # Step 4: Find create a placemark button
    create_place_mark_button = place_mark_page.find_create_a_place_mark_button()
    create_place_mark_button.click()
    place_mark_page.wait_for_visible_element(PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE_SELECTOR)
    local_modal_title = place_mark_page.find_local_modal_title()

    assert local_modal_title.text == PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE, f'The title of the modal is not {PLACE_MARKS_PAGE.LOCALE_MODAL_TITLE}'

    # Step 5:  Find and click waypoint button
    waypoint_button = place_mark_page.find_waypoint_button()
    waypoint_button.click()

    waypoint_modal_title = place_mark_page.find_waypoint_modal_title()
    assert waypoint_modal_title.is_displayed()
    assert waypoint_modal_title.text == PLACE_MARKS_PAGE.WAYPOINT, f'The title of the modal is not {PLACE_MARKS_PAGE.WAYPOINT}'

    # Step 6:  Create waypoint
    input_field = place_mark_page.find_name_input_selector()
    place_mark_page.write_waypoint_name(input_field, PLACE_MARKS_PAGE.TEST_WAYPOINT_NAME)

    ok_button = place_mark_page.find_ok_button()
    ok_button.click()
    sleep(2)
    # Step 7: Find pleacemark icon
    coordinates = place_mark_page.find_place_marks_button()

    # Step 8: Click on the pleacemark icon
    place_mark_page.click_button_at_coordinates(coordinates)
    modal_title = place_mark_page.find_modal_title()
    assert modal_title.text == PLACE_MARKS_PAGE.PLACE_MARKS, f'The title of the modal is not {PLACE_MARKS_PAGE.PLACE_MARKS}'

    # Step 9: Find Displayed placemarks button
    displayed_place_marks_button = place_mark_page.find_displayed_place_marks()
    assert displayed_place_marks_button.text == PLACE_MARKS_PAGE.DISPLAYED_PLACE_MARKS_TEXT,  f'The {PLACE_MARKS_PAGE.DISPLAYED_PLACE_MARKS_TEXT} button is not visible'

    # Step 10: Click Displayed placemarks button
    displayed_place_marks_button.click()

    created_waypoint = place_mark_page.find_created_waypoint()
    assert created_waypoint.text == PLACE_MARKS_PAGE.TEST_WAYPOINT_NAME, f'The {PLACE_MARKS_PAGE.TEST_WAYPOINT_NAME} waypoint is not created'

    # Step 11: Click x button and close modal
    close_modal = place_mark_page.find_close_modal_icon()
    close_modal.click()


