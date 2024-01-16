import pygetwindow as gw

INIT_WIDTH = 932
INIT_HEIGHT = 535
TARGET_EMULATOR = 'NoxPlayer'

def bring_emulator_to_top(emulator_title):
    emulator = gw.getWindowsWithTitle(emulator_title)
    if emulator:
        print(f"Emulator with title '{emulator_title}' found.")
        emulator[0].restore()  # Restore from minimized/maximized state
        emulator[0].activate()
        return True
    else:
        print(f"Emulator with title '{emulator_title}' not found.")
        return False

def get_emulator_window_size(emulator_title):
    emulator = gw.getWindowsWithTitle(emulator_title)
    if emulator:
        width, height = emulator[0].width, emulator[0].height
        print(f"Emulator window size: {width} x {height}")
        return width, height
    else:
        print(f"Emulator with title '{emulator_title}' not found.")
        return False

def resize_emulator_window(emulator_title, width, height):
    emulator = gw.getWindowsWithTitle(emulator_title)
    if emulator:
        emulator[0].resizeTo(width, height)
        print(f"Resized emulator window to {width} x {height}")
        print("Environment initialization complete")
        return True
    else:
        print(f"Emulator with title '{emulator_title}' not found.")
        return False

def environment_initialize(emulator_title=TARGET_EMULATOR):
    if bring_emulator_to_top(emulator_title):
        width, height = get_emulator_window_size(emulator_title)
        if width == INIT_WIDTH and height == INIT_HEIGHT:
            print("Emulator window size is correct. No need to resize.")
            print("Environment initialization complete")
            return True
        else:
            return resize_emulator_window(emulator_title, INIT_WIDTH, INIT_HEIGHT)
    else:
        return False

