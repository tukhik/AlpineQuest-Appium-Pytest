import os
from telnetlib import EC
import cv2
import numpy as np
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from alpineQuest.utils.constants import TIMEOUT, BASE_PAGE


class BasePage:
    def __init__(self, application):
        self.application = application

    def open_application(self):
        try:
            # Execute the adb command to start the app
            result = os.system("adb shell am start -n psyberia.alpinequest.free/.AlpineQuestActivity")

            # Check the result of the command
            if result != 0:
                raise Exception(
                    "Failed to start the app. Please check the package and activity names or the device status.")

            # sleep(5)  # Wait for the app to launch
            WebDriverWait(self.application, TIMEOUT).until(
                EC.presence_of_element_located((AppiumBy.XPATH, BASE_PAGE.ALPINE_QUEST_ELEMENT))
            )
            print("Application started successfully.")

        except Exception as e:
            # Handle the error and display an error message
            print(f"Error: {e}")

    def find(self, args):
        return self.application.find_element(*args)

    def capture_screenshot(self):
        screenshot = self.application.get_screenshot_as_png()
        with open(BASE_PAGE.SCREENSHOT, 'wb') as file:
            file.write(screenshot)
        
        
    def find_and_click_button_by_image(self, button_image_path):
        self.capture_screenshot()

        # Load the screenshot
        screenshot = cv2.imread(BASE_PAGE.SCREENSHOT)

        # Load the button image
        button_image = cv2.imread(button_image_path)

        # Use OpenCV to find the button in the screenshot
        result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Adjust depending on how strict the match should be
        yloc, xloc = np.where(result >= threshold)

        # If a match is found, click on it
        if len(xloc) > 0:
            # Get the location of the first match
            x = xloc[0]
            y = yloc[0]

            # Calculate the center of the matched region
            button_height, button_width = button_image.shape[:2]
            click_x = x + button_width / 2
            click_y = y + button_height / 2

            # Perform the click action
            self.application.tap([(click_x, click_y)])
            print(f'Clicked on button at ({click_x}, {click_y})')
        else:
            print('Button not found')


    