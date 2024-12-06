from time import sleep

from alpineQuest.pages.placemarks_page import PlaceMarks
from utils.constants import PLACE_MARKS_PAGE

def test_route_creation(application):
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

    # Step 5:  Find and click ROUT button
    rout_button = place_mark_page.find_rout_button()
    # Validate that the button is found and clickable
    assert rout_button is not None, "ROUT button is not found"
    assert rout_button.is_displayed() and rout_button.is_enabled(), "ROUT button is either not visible or not clickable"
    # Click the button
    rout_button.click()

    # Step 6:  Find LOCK icon
    place_mark_page.wait_for_visible_element(PLACE_MARKS_PAGE.LOCK_ICON)
    lock_icon = place_mark_page.find_lock_icon()
    assert lock_icon.is_displayed() , "lock icon is not visible or not clickable"

    # Step 7:  Find CANCEL button
    cancel_button = place_mark_page.cancel_button()
    assert cancel_button.is_displayed() and cancel_button.is_enabled(), "Cancel button is either not visible or not clickable"

    # Step 7: Click CANCEL button
    cancel_button.click()
    modal_closed = place_mark_page.waite_until_modal_closed(PLACE_MARKS_PAGE.LOCK_ICON)
    assert modal_closed is None, "Modal is not closed as expected"


