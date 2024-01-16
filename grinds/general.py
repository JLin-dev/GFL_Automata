from util import *

def check_main_menu():
    image_filename = 'images/main_menu/battle_btn.png'
    found, center_cord = find_image(image_filename)
    if found:
        return True, center_cord
    return False, None

