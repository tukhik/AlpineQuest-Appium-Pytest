APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"

DEVICE_NAME = "OnePlus 8"
PLATFORM_NAME = "Android"
PLATFORM_VERSION = "13"
AUTOMATOR_NAME = "uiautomator2"
APP_NAME = "AlpineQuest"
APP_ACTIVITY = ".AlpineQuestActivity"
APP_PACKAGE= "psyberia.alpinequest.free"
TIMEOUT = 10

DESIRED_CAPS = {
    'platformName': PLATFORM_NAME,
    'platformVersion': PLATFORM_VERSION,
    'deviceName': DEVICE_NAME,
    'automationName': AUTOMATOR_NAME,
    'appActivity': APP_ACTIVITY,
    'noReset': True,
    'fullContextList': True,
    'newCommandTimeout': 600,
    'app_package': APP_PACKAGE,
}

class BasePage:
    def __init__(self, alpine_quest_element, screenshot):
        self.ALPINE_QUEST_ELEMENT = alpine_quest_element
        self.SCREENSHOT = screenshot

BASE_PAGE = BasePage(
    '//android.widget.LinearLayout[@resource-id="psyberia.alpinequest.free:id/action_bar_root"]',
    '../screenshots/screen.png'
)

class PositioningPage:
    def __init__(self, switch_off, switch_on, modal_title, menu_button_selector, close_modal_icon, title, text_off, switch_track_recorder_off, lock_icon, cancel_button):
        self.SWITCH_OFF = switch_off
        self.SWITCH_ON = switch_on
        self.MODAL_TITLE = modal_title
        self.MENU_BUTTON_SELECTOR = menu_button_selector
        self.CLOSE_MODAL_ICON = close_modal_icon
        self.TITLE = title
        self.TEXT_OFF = text_off
        self.SWITCH_TRACK_RECORDER_OFF = switch_track_recorder_off
        self.LOCK_ICON = lock_icon
        self.CANCEL_BUTTON = cancel_button

GPS_PAGE = PositioningPage(
    '(//android.widget.Switch[@text="OFF"])[1]',
    '//android.widget.Switch[@text="ON"]',
    '//*[@text="POSITIONING"]',
    '../images/position.png',
    '../images/position_on_red.png',
    'POSITIONING',
    "OFF",
    '(//android.widget.Switch[@text="OFF"])[2]',
    '//android.widget.ImageView[@resource-id="android:id/icon"]',
    '//android.widget.Button[@resource-id="android:id/button2"]'
)

class PlaceMarks:
    def __init__(self,
                 create_place_mark_button,
                 search_location_button,
                 modal_title,
                 locale_modal_title_selector,
                 menu_button_selector,
                 waypoint_text_selector,
                 input_selector,
                 place_marks,
                 waypoint,
                 local_modal_title,
                 test_waypoint_name,
                 ok_button_selector,
                 displayed_place_marks_button,
                 displayed_place_marks_text,
                 crated_waypoint,
                 close_modal_icon,
                 rout_button_selector,
                 lock_icon,
                 cancel_button_selector,
                 search_a_location,
                 search_by_name_selector,
                 location_input_selector,
                 searched_location,
                 search_button_selector,
                 searched_information_selector,
                 display_all_button,
                 search_by_name_button_selector,
                 search_selector,
                 eye_icon_selector,
                 delete_selector,
                 yes_button_selector):
        self.CREATE_PLACE_MARK_BUTTON = create_place_mark_button
        self.SEARCH_LOCATION_BUTTON = search_location_button
        self.MODAL_TITLE = modal_title
        self.LOCALE_MODAL_TITLE_SELECTOR = locale_modal_title_selector
        self.MENU_BUTTON_SELECTOR = menu_button_selector
        self.WAYPOINT_TEXT_SELECTOR = waypoint_text_selector
        self.INPUT_SELECTOR = input_selector
        self.PLACE_MARKS = place_marks
        self.WAYPOINT = waypoint
        self.LOCALE_MODAL_TITLE = local_modal_title
        self.TEST_WAYPOINT_NAME = test_waypoint_name
        self.OK_BUTTON_SELECTOR = ok_button_selector
        self.DISPLAYED_PLACE_MARKS_BUTTON = displayed_place_marks_button
        self.DISPLAYED_PLACE_MARKS_TEXT = displayed_place_marks_text
        self.CRATED_WAYPOINT = crated_waypoint
        self.CLOSE_MODAL_ICON = close_modal_icon
        self.ROUT_BUTTON_SELECTOR = rout_button_selector
        self.LOCK_ICON = lock_icon
        self.CANCEL_BUTTON_SELECTOR = cancel_button_selector
        self.SEARCH_A_LOCATION = search_a_location,
        self.SEARCH_BY_NAME_SELECTOR = search_by_name_selector,
        self.LOCATION_INPUT_SELECTOR = location_input_selector
        self.SEARCHED_LOCATION = searched_location
        self.SEARCH_BUTTON_SELECTOR = search_button_selector
        self.SEARCHED_INFORMATION_SELECTOR = searched_information_selector
        self.DISPLAY_ALL_BUTTON = display_all_button
        self.SEARCH_BY_NAME_BUTTON_SELECTOR = search_by_name_button_selector
        self.SEARCH_SELECTOR = search_selector
        self.EYE_ICON_SELECTOR = eye_icon_selector
        self.DELETE_SELECTOR = delete_selector
        self.YES_BUTTON_SELECTOR = yes_button_selector


PLACE_MARKS_PAGE = PlaceMarks(
    '//android.widget.TextView[@text="Create a placemark"]',
    '//android.widget.TextView[@text="Search a location"]',
    '//android.widget.TextView[@text="PLACEMARKS"]',
    '//android.widget.TextView[@text="LOCAL PLACEMARKS"]',
    '../images/place_marks.png',
    '//android.widget.TextView[@text="Waypoint"]',
    'android.widget.EditText',
    'PLACEMARKS',
    'Waypoint',
    'LOCAL PLACEMARKS',
    'TEST_WAYPOINT',
    '//android.widget.Button[@resource-id="android:id/button1"]',
    '//android.widget.TextView[@text="Displayed placemarks"]',
    'Displayed placemarks',
    '//android.widget.TextView[@text="TEST_WAYPOINT"]',
    '//android.widget.ImageView[@content-desc="Close"]',
    '//android.widget.TextView[@text="Route"]',
    '//android.widget.ImageView[@resource-id="android:id/icon"]',
    '//android.widget.Button[@resource-id="android:id/button2"]',
    '//android.widget.TextView[@text="Search a location"]',
    '//android.widget.TextView[@text="Search by name"]',
    'android.widget.EditText',
    'Vanadzor, Moskovyan 56/2a',
    '//android.widget.Button[@resource-id="android:id/button1"]',
    '//android.widget.TextView[@resource-id="psyberia.alpinequest.free:id/alertTitle"]',
    '// android.widget.Button[ @ resource - id = "android:id/button3"]',
    '//android.widget.TextView[@text="Search by name"]',
    '//android.widget.Button[@resource-id="android:id/button1"]',
    '//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.ImageView',
    '//android.widget.ListView/android.widget.LinearLayout[12]',
    '//android.widget.Button[@resource-id="android:id/button1"]'
)

class CompassPage:
    def __init__(self, compass_button_selector, modal_title_selector, title, screenshot, switch_off, switch_on, close_modal_icon, text_off, compass_off, green_compass):
        self.COMPASS_BUTTON_SELECTOR = compass_button_selector
        self.MODAL_TITLE_SELECTOR = modal_title_selector
        self.TITLE = title
        self.SCREENSHOT = screenshot
        self.SWITCH_OFF = switch_off
        self.SWITCH_ON = switch_on
        self.CLOSE_MODAL_ICON = close_modal_icon
        self.TEXT_OFF = text_off
        self.COMPASS_OFF = compass_off
        self.GREEN_COMPASS = green_compass

COMPASS_PAGE = CompassPage(
    '../images/compass.png',
    '//android.widget.TextView[@text="ORIENTATION"]',
    'ORIENTATION',
    '../screenshots/screen.png',
    '(//android.widget.Switch[@text="OFF"])',
    '//android.widget.Switch[@text="ON"]',
    '../images/green_compass_icon.png',
    'OFF',
    '../images/compass_off_icon.png',
    '../images/green_compass_black_icon.png'
)

class ZoomMapPage:
    def __init__(self, plus_button_selector, minus_button_selector):
        self.PLUS_BUTTON_SELECTOR = plus_button_selector
        self.MINUS_BUTTON_SELECTOR = minus_button_selector

ZOOM_MAP_PAGE = ZoomMapPage(
    '../images/plus.png',
    '../images/minus.png'
)

class AlpineQuestPage:
    def __init__(self, menu_button_selector, title_selector, title, exit_button_selector, exit_button):
        self.MENU_BUTTON_SELECTOR = menu_button_selector
        self.TITLE_SELECTOR = title_selector
        self.TITLE = title
        self.EXIT_BUTTON_SELECTOR = exit_button_selector
        self.EXIT_BUTTON = exit_button

ALPINE_QUEST_PAGE = AlpineQuestPage(
    '../images/app_icon.png',
    './/android.widget.TextView[@text="ALPINEQUEST 2.3.9B"]',
    'ALPINEQUEST 2.3.9B',
    '//android.widget.TextView[@text="Exit"]',
    'Exit'
)


