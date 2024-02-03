import pyautogui
import subprocess
import time
import os

# page pixel size
x_pos = 412
y_pos = 40
width = 689
height = 944

def capture_specific_area_with_screencapture(page_count, save_folder):
    time.sleep(3)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"Note: The folder '{save_folder}' was not found, so it has been created.")

    for i in range(page_count):
        filename = f"{save_folder}/{i+1}.png"

        subprocess.run(["screencapture", "-x", "-R", f"{x_pos},{y_pos},{width},{height}", filename])

        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
