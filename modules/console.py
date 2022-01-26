import os
import time

def clear(args):
    os.system("cls")
def out(args):
    print(" ".join(args).replace("\\n","\n"), end="")
def wait(args):
    time.sleep(float(args[0]))