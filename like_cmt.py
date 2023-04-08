import pyautogui as pg
import keyboard as key
import time
import random

time.sleep(3)
# print(pg.position())

# Open My Browser
pg.leftClick(1012, 1046, 1, 1)
time.sleep(1)

# Open Instagram Web
pg.typewrite("instagram.com/")
pg.press("enter")
time.sleep(5)

# position of search box: x=117, y=358
pg.leftClick(117, 358)
time.sleep(1)
key.write("#python")
time.sleep(2)

# position of hashtag; x=282, y=377
pg.leftClick(282, 377)
time.sleep(7)

# position of image post x=655, y=633
pg.leftClick(655, 633)
time.sleep(1)

list = ["Hi", "Hello", "Hey"]

for i in range(3):
    # position of like button: x=1045, y=832
    pg.leftClick(1045, 832, 1)
    time.sleep(1)

    # position of comment button: x=1099, y=833
    pg.leftClick(1099, 833, 1)
    msg = random.choice(list)
    pg.typewrite(msg)
    time.sleep(1)
    pg.press("enter")
    time.sleep(5)

    # position of next button: x=1794, y=580
    pg.leftClick(1794, 580, 1)
    time.sleep(3)
