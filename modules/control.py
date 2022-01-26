import pyautogui

def mmove(args):
    pyautogui.moveTo(int(args[0]),int(args[1]),duration=float(args[2]))
def mrep(args):
    pyautogui.moveRel(int(args[0]),int(args[1]),duration=float(args[2]))
def mpos(args):
    print(pyautogui.position())
    
def kwrite(args):
    pyautogui.write(" ".join(args))
def kpress(args):
    pyautogui.press(args[0])