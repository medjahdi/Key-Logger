from pynput.mouse import Listener

def WriteToFile(x,y):
    print(f'Position of current moouse: {x} , {y}')

with Listener(on_move=WriteToFile) as l:
    l.join()


#Developed by @medjahdi