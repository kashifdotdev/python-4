import pyautogui
import time
import random

def move_mouse():
    screen_width, screen_height = pyautogui.size()  # Get screen size
    while True:
        # Generate random x and y coordinates within the screen resolution
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        
        # Move the mouse to the new position
        pyautogui.moveTo(x, y, duration=0.5)  # The duration can be adjusted
        
        # Wait for a few seconds before moving the mouse again
        time.sleep(60)  # Move every 60 seconds (adjustable)

if __name__ == "__main__":
    move_mouse()
