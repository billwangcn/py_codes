import pyautogui as pg

try:
    while True:
        if pg.confirm('', '', ['OK', 'Cancel']) == 'OK':
            print(pg.position())
except KeyboardInterrupt:
    print('/n')