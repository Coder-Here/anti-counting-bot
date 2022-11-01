import time
import pyautogui

number = 1

while number<1000:
  pyautogui.write(number)
  number += 2
  time.sleep(2)
