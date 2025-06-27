import pyautogui
import keyboard
import time

def center_click_loop():
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    while True:
        if keyboard.is_pressed('l'):
            break
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
        time.sleep(5)

while True:
    if keyboard.is_pressed('k'):
        center_click_loop()
        break
    elif keyboard.is_pressed('l'):
        break