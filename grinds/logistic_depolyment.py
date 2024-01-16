from util import *

def start_grind_logistic_depolyment():
    environment_initialize()

    # Click redepolyment btn
    image_path = 'images/main_menu/logistic_depolyment_btn.png'
    find_and_click_image(image_path)
    time.sleep(1)

    # Confirm
    image_path = 'images/main_menu/confirm_depoly_logistic_team.png'
    find_and_click_image(image_path)
    time.sleep(1)