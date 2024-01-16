from util import *
from grinds.general import *

TEAM1_OFFSET = (324, 405)
TEAM2_OFFSET = (361, 80)
PLAN_FIRSTPOI_OFFSET = (310, 307)
PLAN_SECONDPOI_OFFSET = (415, 162)
EXCUTE_OFFSET = (770, 430)
def start_grind_81n():
    environment_initialize()
    found, center_cord = check_main_menu()
    if not found:
        print("Please Make Sure Start From Main Menu")
        return
    
    # Click battle_btn from main menu
    random_click_image(center_cord)

    # Click 81n
    image_path = 'images/stages/mission_tab_81n.png'
    wait_for_image_and_click(image_path)

    # Click normal combat
    image_path = 'images/stages/normal_combat_btn.png'
    wait_for_image_and_click(image_path)
    first_time_depoly_81n()
    while True:
        second_part_81n()



def first_time_depoly_81n():
    # Check if enter into the battleground
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = wait_for_image(image_path)
    start_x, start_y = center_cord[0] + 440, center_cord[1] + 320
    end_x, end_y = start_x + 10, start_y + 170
    pyautogui.click(start_x, start_y)
    pyautogui.keyDown('ctrlleft')
    pyautogui.scroll(-50)
    pyautogui.keyUp('ctrlleft')
    time.sleep(0.5)
    pyautogui.click(start_x, start_y)
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=1)  # Adjust duration as needed
    pyautogui.mouseUp()
    end_x, end_y = start_x, start_y - 92
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=1)  # Adjust duration as needed
    pyautogui.mouseUp()

    # Depoly second team (refill team)
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = wait_for_image(image_path)
    random_click_image((center_cord[0] + TEAM2_OFFSET[0], center_cord[1] + TEAM2_OFFSET[1]))
    
    # Choose second team tab
    image_path = 'images/stages/second_team_tab.png'
    wait_for_image_and_click(image_path)

    # Confirm depoly second team 
    image_path = 'images/stages/confirm_depoly_btn.png'
    wait_for_image_and_click(image_path)

    # Depoly first team
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = wait_for_image(image_path)
    random_click_image((center_cord[0] + TEAM1_OFFSET[0], center_cord[1] + TEAM1_OFFSET[1]))
    
    # Confirm depoly first team 
    image_path = 'images/stages/confirm_depoly_btn.png'
    wait_for_image_and_click(image_path)

def second_part_81n():
    # Start Combat
    image_path = 'images/stages/start_combat_btn.png'
    wait_for_image_and_click(image_path)

    # Refill team
    image_path = 'images/stages/end_round_btn.png'
    found, center_cord = wait_for_image(image_path)
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = find_image(image_path)
    time.sleep(1)
    # Select team
    random_click_image((center_cord[0] + TEAM2_OFFSET[0], center_cord[1] + TEAM2_OFFSET[1]))
    time.sleep(0.5)
    # Open refill menu
    random_click_image((center_cord[0] + TEAM2_OFFSET[0], center_cord[1] + TEAM2_OFFSET[1]))

    # Resupply the team
    image_path = 'images/stages/supply_btn.png'
    found = wait_for_image_and_click(image_path, timeout=5)
    while not found:
        random_click_image((center_cord[0] + TEAM2_OFFSET[0], center_cord[1] + TEAM2_OFFSET[1]))
        found = wait_for_image_and_click(image_path, timeout=5)
    random_click_image((center_cord[0] + TEAM2_OFFSET[0], center_cord[1] + TEAM2_OFFSET[1]))

    # Retreat the resupply team
    image_path = 'images/stages/retreat_btn.png'
    wait_for_image_and_click(image_path)

    # Confirm retreat
    image_path = 'images/stages/confirm_retreat_btn.png'
    wait_for_image_and_click(image_path)

    # Select team 1 with plan mode clicking differnt POI
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = wait_for_image(image_path)
    time.sleep(1)
    # Select team
    random_click_image((center_cord[0] + TEAM1_OFFSET[0], center_cord[1] + TEAM1_OFFSET[1]))
    image_path = 'images/stages/plan_mode.png'
    wait_for_image_and_click(image_path)
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = wait_for_image(image_path)
    random_click_image((center_cord[0] + PLAN_FIRSTPOI_OFFSET[0], center_cord[1] + PLAN_FIRSTPOI_OFFSET[1]))
    random_click_image((center_cord[0] + PLAN_SECONDPOI_OFFSET[0], center_cord[1] + PLAN_SECONDPOI_OFFSET[1]))
    random_click_image((center_cord[0] + EXCUTE_OFFSET[0], center_cord[1] + EXCUTE_OFFSET[1]))

    # Restart combat once is on last move
    image_path = 'images/stages/last_move.png'
    time.sleep(104)
    wait_for_image(image_path)
    time.sleep(22)
    wait_for_image(image_path)
    image_path = 'images/stages/stop_combat_btn.png'
    wait_for_image_and_click(image_path)
    image_path = 'images/stages/restart_combat_btn.png'
    wait_for_image_and_click(image_path)

    # Once get into combat we need to perform team member swap
    image_path = 'images/stages/start_combat_btn.png'
    wait_for_image(image_path)
    image_path = 'images/stages/mission_choice_btn.png'
    found, center_cord = wait_for_image(image_path)
    random_click_image((center_cord[0] + TEAM1_OFFSET[0], center_cord[1] + TEAM1_OFFSET[1]))

    # Edit team
    image_path = 'images/stages/edit_team_btn.png'
    wait_for_image_and_click(image_path)
    time.sleep(2)

    #Select Zas
    image_path = 'images/edit_team/select_Zas.png'
    wait_for_image_and_click(image_path)

    #Select Type
    image_path = 'images/edit_team/select_type.png'
    wait_for_image_and_click(image_path)

    #Select five star
    image_path = 'images/edit_team/five_star.png'
    wait_for_image_and_click(image_path)

    #Select assult rifle
    image_path = 'images/edit_team/assult_rifle.png'
    wait_for_image_and_click(image_path)

    #Select confirm filter 
    image_path = 'images/edit_team/confirm_filter.png'
    wait_for_image_and_click(image_path)
    
    #Select second zas 
    image_path = 'images/edit_team/second_Zas.png'
    wait_for_image_and_click(image_path)

    # Back to combact
    image_path = 'images/edit_team/back_to_combat.png'
    wait_for_image_and_click(image_path)
