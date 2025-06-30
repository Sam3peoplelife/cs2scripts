# CS2 Scripts

This repository contains two Python scripts for automating actions in Counter-Strike 2 using the `pyautogui` and `keyboard` libraries.
Working with 4:3 resolution

## Contents

- [autoAcceptingMatch.py](autoAcceptingMatch.py) — automatic match acceptance.
- [autoReportScript.py](autoReportScript.py) — automating the reporting process.

---

## Requirements

- Python 3.x
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [keyboard](https://pypi.org/project/keyboard/)

Install dependencies with:
```sh
pip install pyautogui keyboard
```

---

## Script Descriptions

### [autoAcceptingMatch.py](autoAcceptingMatch.py)

Automatically clicks in the center of the screen every 5 seconds until the `l` key is pressed.  
Start the loop — press `k`.  
Stop — press `l`.

### [autoReportScript.py](autoReportScript.py)

Automates the reporting process in the game.  
Start automation — press `k`.  
Stop the script — press `l`.

---

## Usage

1. Run the desired script:
    ```sh
    python autoAcceptingMatch.py
    ```
    or
    ```sh
    python autoReportScript.py
    ```
2. Follow the hotkey instructions (`k` to start, `l` to stop).