from tkinter import messagebox

def msgboxinfo(args):
    messagebox.showinfo(args[0], args[1])
def msgboxerror(args):
    messagebox.showerror(args[0], args[1])
def msgboxwarning(args):
    messagebox.showwarning(args[0], args[1])