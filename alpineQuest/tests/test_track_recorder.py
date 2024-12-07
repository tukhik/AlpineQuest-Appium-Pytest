from appium.webdriver.common.appiumby import AppiumBy

from alpineQuest.pages.gps_page import PositioningPage
from alpineQuest.utils.constants import GPS_PAGE


def test_track_recorder(application):
    # Step 1: Open the app.
    gps_page = PositioningPage(application)
    gps_page.open_app()
    # The app is successfully launched.

    # Step 2: Find GPS icon
    coordinates = gps_page.find_gps_button()

    # Step 3: Click GPS icon
    gps_page.click_button_at_coordinates(coordinates)
    modal_title = gps_page.find_modal_title()

    assert modal_title.text == GPS_PAGE.TITLE, f'The title of the modal is not {GPS_PAGE.TITLE}'

    # Step 4: Switch on Track recorder
    track_recorder = gps_page.find_element_by_xpath(GPS_PAGE.SWITCH_TRACK_RECORDER_OFF)

    track_recorder.click()

    # Step 5:  Find LOCK icon
    gps_page.wait_for_visible_element(GPS_PAGE.LOCK_ICON)
    lock_icon = gps_page.find_element_by_xpath(GPS_PAGE.LOCK_ICON)
    assert lock_icon.is_displayed(), "lock icon is not visible or not clickable"

    # Step 6:  Find CANCEL button
    cancel_button = gps_page.find_element_by_xpath(GPS_PAGE.CANCEL_BUTTON)
    assert cancel_button.is_displayed() and cancel_button.is_enabled(), "Cancel button is either not visible or not clickable"

    # Step 7: Click CANCEL button
    cancel_button.click()
    modal_closed = gps_page.waite_until_modal_closed(GPS_PAGE.LOCK_ICON)
    assert modal_closed is None, "Modal is not closed as expected"

    # Step 8: Click GPS button and close modal
    gps_page.close_gps_modal()

    # Step 9: Verify GPS modal is closed
    modal_closed = gps_page.waite_until_modal_closed(GPS_PAGE.MODAL_TITLE)
    assert modal_closed is None, "Modal is not closed as expected"

