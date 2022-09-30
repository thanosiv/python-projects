# need pyautogui to be able to "move" the mouse
import pyautogui
# need time to be able to specify when to rerun
import time

# while True in this case means while the script is running
while True:
    # pyautogui.moveRel(xOffset,yOffset); relative to current position of cursor
    pyautogui.moveRel(0, 10)
    # how much time will pass before pyautogui.moveRel runs again; in this case, every 5 seconds
    time.sleep(5)
