import pyautogui
import keyboard
import time
from datetime import datetime

def log_action(message):
    with open("report_log.txt", "a") as log_file:
        log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def auto_report(iterations=10):
    x0, y0 = pyautogui.position()
    for i in range(iterations):
        pyautogui.click()
        log_action(f"Clicked at ({x0}, {y0}) - iteration {i+1}")

        pyautogui.moveTo(x0 + 350, y0 + 100)
        time.sleep(0.2)
        pyautogui.click()
        log_action(f"Clicked at ({x0 + 350}, {y0 + 100})")

        pyautogui.moveTo(950, 540)
        time.sleep(0.2)
        pyautogui.click()
        log_action("Clicked at (950, 540)")

        pyautogui.moveTo(930, 710)
        pyautogui.click()
        log_action("Clicked at (930, 710)")

        pyautogui.moveTo(x0, y0)
        time.sleep(0.1)
        log_action(f"Returned to ({x0}, {y0})")

def main():
    print("Press 'k' to start auto report, 'l' to exit.")
    while True:
        if keyboard.is_pressed('k'):
            auto_report()
        elif keyboard.is_pressed('l'):
            print("Exiting script.")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()