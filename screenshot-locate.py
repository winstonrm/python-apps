import cv2
import numpy as np
import pyautogui as pg

def click(button):
    pg.mouseDown(button=button)
    pg.mouseUp(button=button)

# screenshot = pg.screenshot()
# screenshot.save(r'C:\wprojetos\python\WebScraping\project1\img-pyautogui\screenshot.png')

# screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

icon = pg.locateOnScreen(r'C:\wprojetos\python\WebScraping\project1\img-pyautogui\pular.png')
print(icon)
pg.click(icon, button = 'left')
click('left')

# cv2.imshow('screenshot', screenshot)

# cv2.waitKey(0)

# cv2.destroyAllWindows()