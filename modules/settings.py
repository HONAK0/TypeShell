def setusername(args):
    open("C:/TypeShell/userdata/username", "w", encoding="utf8").write(args[0])
def setstartup(args):
    open("C:/TypeShell/userdata/startup", "w", encoding="utf8").write(" ".join(args))