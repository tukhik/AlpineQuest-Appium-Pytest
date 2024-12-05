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
    def __init__(self, ALPINE_QUEST_ELEMENT, SCREENSHOT):
        self.ALPINE_QUEST_ELEMENT = ALPINE_QUEST_ELEMENT  # Attribute for make
        self.SCREENSHOT = SCREENSHOT  # Attribute for model

BASE_PAGE = BasePage(
    '//android.widget.LinearLayout[@resource-id="psyberia.alpinequest.free:id/action_bar_root"]',
    './screenshots/screen.png'
)

class PositioningPage:
    def __init__(self, SWITCH_OFF, SWITCH_ON, MODAL_TITLE, MENU_BUTTON_SELECTOR, CLOSE_MODAL_ICON, TITLE, TEXT_OFF):
        self.SWITCH_OFF = SWITCH_OFF
        self.SWITCH_ON = SWITCH_ON
        self.MODAL_TITLE = MODAL_TITLE
        self.MENU_BUTTON_SELECTOR = MENU_BUTTON_SELECTOR
        self.CLOSE_MODAL_ICON = CLOSE_MODAL_ICON
        self.TITLE = TITLE
        self.TEXT_OFF = TEXT_OFF

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
                 CREATE_PLACE_MARK_BUTTON,
                 MODAL_TITLE,
                 LOCALE_MODAL_TITLE_SELECTOR,
                 MENU_BUTTON_SELECTOR,
                 WAYPOINT_TEXT_SELECTOR,
                 INPUT_SELECTOR,
                 PLACE_MARKS,
                 WAYPOINT,
                 LOCAL_MODAL_TITLE,
                 TEST_WAYPOINT_NAME,
                 OK_BUTTON_SELECTOR,
                 DISPLAYED_PLACE_MARKS_BUTTON,
                 DISPLAYED_PLACE_MARKS_TEXT,
                 CRATED_WAYPOINT,
                 CLOSE_MODAL_ICON):
        self.CREATE_PLACE_MARK_BUTTON = CREATE_PLACE_MARK_BUTTON
        self.MODAL_TITLE = MODAL_TITLE
        self.LOCALE_MODAL_TITLE_SELECTOR = LOCALE_MODAL_TITLE_SELECTOR
        self.MENU_BUTTON_SELECTOR = MENU_BUTTON_SELECTOR
        self.WAYPOINT_TEXT_SELECTOR = WAYPOINT_TEXT_SELECTOR
        self.INPUT_SELECTOR = INPUT_SELECTOR
        self.PLACE_MARKS = PLACE_MARKS
        self.WAYPOINT = WAYPOINT
        self.LOCALE_MODAL_TITLE = LOCAL_MODAL_TITLE
        self.TEST_WAYPOINT_NAME = TEST_WAYPOINT_NAME
        self.OK_BUTTON_SELECTOR = OK_BUTTON_SELECTOR
        self.DISPLAYED_PLACE_MARKS_BUTTON = DISPLAYED_PLACE_MARKS_BUTTON
        self.DISPLAYED_PLACE_MARKS_TEXT = DISPLAYED_PLACE_MARKS_TEXT
        self.CRATED_WAYPOINT = CRATED_WAYPOINT
        self.CLOSE_MODAL_ICON = CLOSE_MODAL_ICON

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

