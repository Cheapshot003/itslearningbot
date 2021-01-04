#Alpha Version 0.2 | Proof of Concept

import pyautogui
from time import sleep

print("Tietzers itslearning Bot")
print("-------------------------")

screenResX = int(input("Bildschirmauflösung X (X*Y):"))
screenResY = int(input("Bildschirmauflösung Y (X*Y):"))
timeout = int(input("Wie viele Sekunden möchtest du in jedem Kurs verbringen?"))

print("\n\nBitte Fenster minimiren und Browser maximieren")
print("Start in 5 Sekunden")
sleep(5)

def getX(x):
    x1 = 320 + (x*310) - 310
    x2 = x1 / screenResX
    return x2 * screenResX


def getY(y):
    y1 = 446 + (y*310) - 310
    y2 = y1 / screenResY
    return y2 * screenResY

def clickCourse(x,y):
    pyautogui.moveTo(getX(x), getY(y))
    pyautogui.click()

def goStart():
    pyautogui.moveTo(0.016625*screenResX,0.1029518*screenResY)
    pyautogui.click()

def scrolldown():
    pyautogui.moveTo(0.9963541*screenResX,0.201851851*screenResY)
    pyautogui.dragRel(0,0.37037037*screenResY,duration=1)

print(pyautogui.position())

#clickCourse(1,1)

goStart()
sleep(2)
print("Click")
clickCourse(1,1)
sleep(timeout)

goStart()
sleep(2)
print("Click")
clickCourse(2, 1)
sleep(timeout)

goStart()
sleep(2)
clickCourse(3,1)
sleep(timeout)

goStart()
sleep(2)
clickCourse(4,1)
sleep(timeout)

goStart()
sleep(2)
clickCourse(5,1)
sleep(timeout)
goStart()
sleep(2)

goStart()
sleep(2)
clickCourse(1,2)
sleep(timeout)

goStart()
sleep(2)
clickCourse(2,2)
sleep(timeout)

goStart()
sleep(2)
clickCourse(3,2)
sleep(timeout)

goStart()
sleep(2)
clickCourse(4,2)
sleep(timeout)

goStart()
sleep(2)
clickCourse(5,2)
sleep(timeout)

goStart()
sleep(2)
scrolldown()

