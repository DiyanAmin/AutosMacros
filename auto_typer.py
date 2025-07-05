import pyautogui as pg
import time as t
text=input('Enter text to type: ')
sfs=bool(input('Set failsafe to: '))
pg.FAILSAFE=sfs
grace_period=int(input('Delay(in seconds) before starting: '))
repeat=int(input('Number of times to repeat program(965354 for infinite): '))
def rep(repeat,text):
    for i in range(repeat):
        pg.typewrite(text)
        t.sleep(delay)
    print('Done')
delay=int(input('Text writing delay: '))
def inf(text):
    while True:
        pg.typewrite(text)
        t.sleep(delay)
if repeat==965354:
    inf(text)
else:
    delay=int(input('Text writing delay: '))
    print('Starting Grace Period!')
    t.sleep(grace_period)
    rep(repeat,text)