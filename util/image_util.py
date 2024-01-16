import cv2
import pyautogui
import numpy as np
import os
import random
import time

def find_image(image_path, threshold=0.8):
    image_title = os.path.basename(image_path)

    # Read the image
    # template = cv2.imread(image_path)

    # Read the image in grayscale
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to OpenCV format (BGR)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)


    # Match the template in the screenshot
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        print(f"Found image: {image_title}")
        # Get the coordinates of the matched area
        match_x, match_y = max_loc

        # Get the width and height of the template image
        h, w = template.shape

        # Calculate the center of the matched area
        center_x = match_x + w // 2
        center_y = match_y + h // 2
        return True, (center_x, center_y)
    else:
        print(f"Image not found: {image_path}")
        return False, None

def random_click_image(center_cord):
    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    new_x = center_cord[0] + offset_x
    new_y = center_cord[1] + offset_y
    pyautogui.moveTo(new_x, new_y)
    time.sleep(0.05)
    pyautogui.click()


def find_and_click_image(image_path, threshold=0.8):
    found, center_cord = find_image(image_path, threshold)
    if found:
        random_click_image(center_cord)
        return True
    else:
        return False
    

def wait_for_image(image_path, timeout=999999, threshold=0.8):
    start_time = time.time()

    while time.time() - start_time < timeout:
        found, center_cord = find_image(image_path, threshold)
        if found:
            return True, center_cord

        time.sleep(1)  # Adjust the sleep duration based on your needs

    print("Wait for image time out")
    return False, None

def wait_for_image_and_click(image_path, timeout=999999, threshold=0.8):
    start_time = time.time()

    while time.time() - start_time < timeout:
        found, center_cord = find_image(image_path, threshold)
        if found:
            time.sleep(1)
            random_click_image(center_cord)
            return True

        time.sleep(1)  # Adjust the sleep duration based on your needs

    print("Wait for image time out")
    return False
