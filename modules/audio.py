from pygame import mixer
import pygame
from tkinter import messagebox

try:
    mixer.init()
except:
    messagebox.showinfo("TypeShell | PyGame Mixer","Подключите устройство для воиспроизведения звука или прибавьте громкость")
    
def playaudio(args): 
    mixer.music.load(args[0])
    mixer.music.play()
def stopaudio(args):
    mixer.music.stop()