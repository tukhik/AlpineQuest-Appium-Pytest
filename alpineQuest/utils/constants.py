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

PLACE_MARKS = "PLACEMARKS"
LOCAL_PLACE_MARKS = 'LOCAL PLACEMARKS'
WAYPOINT = 'Waypoint'
