import pyautogui
import keyboard
import time
from datetime import datetime

x1, y1 = 350, 100
x2, y2 = 950, 540
x3, y3 = 930, 710
delay1 = 0.2
delay2 = 0.1

def log_action(message):
    with open("report_log.txt", "a") as log_file:
        log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def auto_report(iterations=10):
    x0, y0 = pyautogui.position()
    for i in range(iterations):
        pyautogui.click()
        log_action(f"Clicked at ({x0}, {y0}) - iteration {i+1}")

        pyautogui.moveTo(x0 + x1, y0 + y1)
        time.sleep(delay1)
        pyautogui.click()
        log_action(f"Clicked at ({x0 + 350}, {y0 + 100})")

        pyautogui.moveTo(x2, y2)
        time.sleep(delay1)
        pyautogui.click()
        log_action("Clicked at (950, 540)")

        pyautogui.moveTo(x3, y3)
        pyautogui.click()
        log_action("Clicked at (930, 710)")

        pyautogui.moveTo(x0, y0)
        time.sleep(delay2)
        log_action(f"Returned to ({x0}, {y0})")

def main():
    print("Press 'k' to start auto report, 'l' to exit.")
    while True:
        if keyboard.is_pressed('k'):
            auto_report()
        elif keyboard.is_pressed('l'):
            print("Exiting script.")
            break
        time.sleep(delay2)

if __name__ == "__main__":
    main()