#Alpha Version 0.1 | Proof of Concept

import pyautogui
from time import sleep


def getX(x):
    return 320 + (x*310) - 310


def getY(y):
    return 446 + (y*310) - 310


def clickCourse(x,y):
    pyautogui.moveTo(getX(x), getY(y))
    pyautogui.click()

def goStart():
    pyautogui.moveTo(30,100)
    pyautogui.click()

def scrolldown():
    pyautogui.moveTo(1913,218)
    pyautogui.dragRel(0,400,duration=1)

print(pyautogui.position())

#clickCourse(1,1)

goStart()
sleep(2)
clickCourse(1,1)
sleep(5)

goStart()
sleep(2)
clickCourse(2, 1)
sleep(5)

goStart()
sleep(2)
clickCourse(3,1)
sleep(5)

goStart()
sleep(2)
clickCourse(4,1)
sleep(5)

goStart()
sleep(2)
clickCourse(5,1)
sleep(5)
goStart()
sleep(2)

goStart()
sleep(2)
clickCourse(1,2)
sleep(5)

goStart()
sleep(2)
clickCourse(2,2)
sleep(5)

goStart()
sleep(2)
clickCourse(3,2)
sleep(5)

goStart()
sleep(2)
clickCourse(4,2)
sleep(5)

goStart()
sleep(2)
clickCourse(5,2)
sleep(5)

goStart()
sleep(2)
scrolldown()
