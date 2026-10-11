import keyboard
import time
import mouse
def click():
    keyboard.press_and_release("4")
    mouse.click("right")
    mouse.click("right")
    time.sleep(0.05)
    keyboard.press_and_release("3")
    mouse.click("right")

keyboard.add_hotkey("shift+z",click)
keyboard.add_hotkey("z",click)
#mouse.on_button(click, buttons="x", types=("down",))

mouse.wait("9")