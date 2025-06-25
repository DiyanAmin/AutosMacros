import pyautogui as  pg
import time
delay=int(input('Enter grace period(seconds): '))
set_failsafe=bool(input('Set FAILSAFE to: '))
pg.FAILSAFE=set_failsafe
func=str(input('Function to use: '))
auto_clicker=''
def autoclicker(func):
    tp=str(input('Click type( right or left): '))
    if tp=='left':
        time.sleep(delay)
        while True:
            pg.click()
    elif tp=='right':
        time.sleep(delay)
        while True:
            pg.rightClick()
    elif tp=='middle':
        time.sleep(delay)
        while True:
            pg.middleClick()
    else:
        print('IDK')
def delay_click(func):
    delay_type=str(input('Enter unit of delay(sec or min): '))
    delay_time=int(input('Enter delay: '))
    if delay_type=='sec':
        pass
    elif delay_type=='min':
        delay_time*=60
    else:
        print('Invalid')
    time.sleep(delay)
    while True:
        pg.click()
        time.sleep(delay_time)
if func=='autoclicker':
    autoclicker(func)
elif func=='delayed':
    delay_click(func)
else:
    print('Code not written')