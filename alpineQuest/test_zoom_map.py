from time import sleep

from alpineQuest.pages.zoom_map_page import ZoomMapPage
from utils.constants import ZOOM_MAP_PAGE

def test_zoom_map(application):
    # Step 1: Open the app.
    zoom_map_page = ZoomMapPage(application)
    zoom_map_page.open_app()
    # The app is successfully launched.

    # Step 2: Fined + icon
    coordinates_plus_icon = zoom_map_page.fined_plus_button()
    assert coordinates_plus_icon is not None, "coordinates_plus_icon is invalid or not found"

    # Step 3: Click + icon
    zoom_map_page.click_plus_button(coordinates_plus_icon)
    sleep(1)

    # Step 4: Fined - icon
    coordinates_minus_icon = zoom_map_page.fined_minus_button()
    assert coordinates_minus_icon is not None, "coordinates_minus_icon is invalid or not found"

    # Step 5: Click - icon
    zoom_map_page.click_minus_button(coordinates_minus_icon)