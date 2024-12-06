from time import sleep

from alpineQuest.pages.placemarks_page import PlaceMarks
from utils.constants import PLACE_MARKS_PAGE

def test_search_by_name(application):
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

    # Step 4: Find and click "search a location" button
    search_location_button = place_mark_page.find_search_location_button()
    search_location_button.click()
    # place_mark_page.wait_for_visible_element(PLACE_MARKS_PAGE.SEARCH_BY_NAME_SELECTOR)

    # Step 5: Find and click "search by name" button
    search_by_name_button = place_mark_page.find_search_by_name_button()
    assert search_by_name_button is not None, "search_by_name_button is not found"

    search_by_name_button.click()

    # Step 6: Fill Search by name field
    input_field = place_mark_page.find_search_location_input()

    # Step 6: Fill Search by name field
    place_mark_page.write_search_location_name(input_field, PLACE_MARKS_PAGE.SEARCHED_LOCATION)

    # Step 7: Find and click search button
    search_button = place_mark_page.find_search_button()
    assert search_button is not None, "search_button is not found"
    search_button.click()

    place_mark_page.wait_for_visible_element(PLACE_MARKS_PAGE.SEARCH_MODAL_TITLE_SELECTOR)

    # Step 8: Get find data
    searched_information = place_mark_page.find_searched_information_title()

    assert searched_information.text() ==  PLACE_MARKS_PAGE.SEARCHED_LOCATION, "search_button is not found"

    # Step 9: Close information modal

    display_all_button = place_mark_page.find_display_all_button()
    assert display_all_button is not None, "display_all_button is not found"

    display_all_button.click()
