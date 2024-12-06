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
        self.ALPINE_QUEST_ELEMENT = alpine_quest_element  # Attribute for make
        self.SCREENSHOT = screenshot  # Attribute for model

BASE_PAGE = BasePage(
    '//android.widget.LinearLayout[@resource-id="psyberia.alpinequest.free:id/action_bar_root"]',
    './screenshots/screen.png'
)

class PositioningPage:
    def __init__(self, switch_off, switch_on, modal_title, menu_button_selector, close_modal_icon, title, text_off):
        self.SWITCH_OFF = switch_off
        self.SWITCH_ON = switch_on
        self.MODAL_TITLE = modal_title
        self.MENU_BUTTON_SELECTOR = menu_button_selector
        self.CLOSE_MODAL_ICON = close_modal_icon
        self.TITLE = title
        self.TEXT_OFF = text_off

GPS_PAGE = PositioningPage(
    '(//android.widget.Switch[@text="OFF"])[1]',
    '//android.widget.Switch[@text="ON"]',
    '//*[@text="POSITIONING"]',
    './images/position.png',
    './images/position_on_red.png',
    'POSITIONING',
    "OFF"
)

class PlaceMarks:
    def __init__(self,
                 create_place_mark_button,
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
                 close_modal_icon):
        self.CREATE_PLACE_MARK_BUTTON = create_place_mark_button
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

PLACE_MARKS_PAGE = PlaceMarks(
    '//android.widget.TextView[@text="Create a placemark"]',
    '//android.widget.TextView[@text="PLACEMARKS"]',
    '//android.widget.TextView[@text="LOCAL PLACEMARKS"]',
    './images/place_marks.png',
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
    '//android.widget.ImageView[@content-desc="Close"]'
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
    './images/compass.png',
    '//android.widget.TextView[@text="ORIENTATION"]',
    'ORIENTATION',
    './screenshots/screen.png',
    '(//android.widget.Switch[@text="OFF"])',
    '//android.widget.Switch[@text="ON"]',
    './images/green_compass_icon.png',
    'OFF',
    './images/compass_off_icon.png',
    './images/green_compass_black_icon.png'
)

class ZoomMapPage:
    def __init__(self, plus_button_selector, minus_button_selector):
        self.PLUS_BUTTON_SELECTOR = plus_button_selector
        self.MINUS_BUTTON_SELECTOR = minus_button_selector

ZOOM_MAP_PAGE = ZoomMapPage(
    './images/plus.png',
    './images/minus.png'
)

