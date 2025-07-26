#Macros with Custom
macroSel=input('Macro: ')
#Mouse macros
import pyautogui as  pg
import time
def mouse_macro(macroSel):
    delay=int(input('Enter grace period(seconds): '))
    set_failsafe=bool(input('Set FAILSAFE to: '))
    pg.FAILSAFE=set_failsafe
    func=str(input('Function to use: '))
    auto_clicker=''
    def autoclicker(func):
        tp=str(input('Click type(right|middle|left): '))
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

#Pre-Defined Macros

class Macros:
    def Walk(self,duration,extra_key):
        print('This macro will afk walk for you (W key) if you have extra keys during this time, fill in the following')
        extra_key=str(input('Extra Key(none if no key): '))
        if extra_key!='none':
            pg.hold('w')
            time.sleep(1)
            pg.hold(extra_key)
        else:
            pg.hold('w')
#Custom Macro Interface

class CustomMacro:
    grace_period=int(input('Delay before start: '))
    save_load=str(input('Load or Save a macro?: '))
    if save_load=='Load':
        macroNum=int(input('Macro Number: '))
    def customMacro1(self,text):
        macroType=str(input('Macro type(keypress | mouse | both): '))
        if macroType=='both':
            print("Place Holder")