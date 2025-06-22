import pyautogui
import keyboard
import time

def autoReport():
    for _ in range(10):
            pyautogui.click()
            x0, y0 = pyautogui.position()

            pyautogui.moveTo(x0 + 350, y0 + 100)
            time.sleep(0.2)
            pyautogui.click()

            pyautogui.moveTo(950,540)
            time.sleep(0.2)
            pyautogui.click()

            pyautogui.moveTo(930, 710)
            pyautogui.click()
            
            pyautogui.moveTo(x0, y0)
            time.sleep(0.1)

while True:
    if keyboard.is_pressed('k'):
        autoReport()
    elif keyboard.is_pressed('l'):
        break
    else:
         continue