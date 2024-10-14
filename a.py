import autoit
import time

try:
    autoit.run('mspaint.exe')
    time.sleep(2)
    x1 = 650, y1 = 500, x2 = 800, y2=250
    x1 = 800, y1 = 250, x2 = 650, y2=500
    autoit.mouse_click_drag(x1=x1, y1=y1, x2=x2, y2=y2, button="left")
    autoit.mouse_click_drag(x1=x1, y1=y1, x2=x2, y2=y2, button="left")
except Exception as e:
    print(e)