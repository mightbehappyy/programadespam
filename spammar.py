from re import I
import pyautogui as pg
import time

time.sleep(5)
txt = open('scriptshrek2.txt', 'r')

for word in txt:
    pg.typewrite(word)
    pg.press('Enter')