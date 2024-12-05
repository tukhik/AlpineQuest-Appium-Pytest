APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"

DEVICE_NAME = "OnePlus 8"
PLATFORM_NAME = "Android"
PLATFORM_VERSION = "13"
AUTOMATOR_NAME = "uiautomator2"
APP_NAME = "AlpineQuest"
APP_ACTIVITY = ".AlpineQuestActivity"
APP_PACKAGE= "psyberia.alpinequest.free"

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

TIMEOUT = 10

class BasePage:
    def __init__(self, ALPINE_QUEST_ELEMENT, model, year):
        self.ALPINE_QUEST_ELEMENT = ALPINE_QUEST_ELEMENT  # Attribute for make
        self.model = model  # Attribute for model
        self.year = year  # Attribute for year

    def display_info(self):
        print(f"Car: {self.ALPINE_QUEST_ELEMENT} {self.make} {self.model}")


# Create an object (instance) of the Car class
BASE_PAGE = BasePage('//android.widget.LinearLayout[@resource-id="psyberia.alpinequest.free:id/action_bar_root"]', "Camry", 2020)

GPS_PAGE_TITLE = 'POSITIONING'
OFF = "OFF"
PLACE_MARKS = "PLACEMARKS"
LOCAL_PLACE_MARKS = 'LOCAL PLACEMARKS'
WAYPOINT = 'Waypoint'
