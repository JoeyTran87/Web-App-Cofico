#! python3
# main.py - CONTROL MOUSE
import pyautogui, time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.size()
width, height = pyautogui.size()

print(width, height)
#-----------------------------------------#
# MOVE MOUSE BY EXCACT POSITON
#-----------------------------------------#
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
#-----------------------------------------#
# MOVE MOUSE FROM RELATIVE POSITON
#-----------------------------------------#
# for i in range(10):
while True:
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)


#-----------------------------------------#
# GET MOUSE POSTION
#-----------------------------------------#
# try:
#     while True:
#         print(pyautogui.position())
#         time.sleep(5)
# except KeyboardInterrupt:
#     quit()

#-----------------------------------------#
# MOUSE CLICK
#-----------------------------------------#

# try:
#     while True:
#         pyautogui.click(1806, 14)
#         time.sleep(2)
# except KeyboardInterrupt:
#     quit()