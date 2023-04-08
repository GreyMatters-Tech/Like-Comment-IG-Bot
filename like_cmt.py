import pyautogui as pg
import keyboard as key
import time
import random

time.sleep(3)
# print(pg.position())

# Open My Browser
pg.leftClick(944, 1042, 1, 1)
time.sleep(1)

# Open Instagram Web
pg.typewrite("instagram.com/")
pg.press("enter")
time.sleep(1)

# position of search box: x=643, y=103
pg.leftClick(643, 103)
time.sleep(1)
key.write("#python")
time.sleep(2)

# position of hashtag; x=650, y=164
pg.leftClick(650, 164)
time.sleep(3)

# position of image post x=314, y=529
pg.leftClick(314, 529)
time.sleep(3)

list = ["Hello#python", "Hi", "Hey"]

for i in range(5):
    # position of like button: x=729, y=566
    time.sleep(1)

    # position of comment button: x=888, y=680
    pg.leftClick(888, 688, 1)
    msg = random.choice(list)
    pg.typewrite(msg)
    time.sleep(1)
    pg.press("enter")
    time.sleep(5)

    # position of next button: x=1322, y=391
    pg.leftClick(1322, 391)
    time.sleep(3)
