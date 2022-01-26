try:
    import getpass
    import os
    import sys

    os.system("cls")
    print("Загрузка...")
    def m(path):
        print(f"Creating '{path}'...")
        os.mkdir(path)
    def r(name):
        return open(name,"r",encoding="utf8").read()
    def w(name, value):
        open(name,"w",encoding="utf8").write(value)
    if not os.path.exists("C:/TypeShell"):
        m("C:/TypeShell")
    if not os.path.exists("C:/TypeShell/userdata"):
        m("C:/TypeShell/userdata")
    if not os.path.exists("C:/TypeShell/modules"):
        m("C:/TypeShell/modules")
    if not os.path.exists("C:/TypeShell/userdata/username"):
        username = getpass.getuser()
        w("C:/TypeShell/userdata/username", username)
    if not os.path.exists("C:/TypeShell/userdata/startup"):
        username = getpass.getuser()
        w("C:/TypeShell/userdata/startup", "Привет!")
    username = r("C:/TypeShell/userdata/username")
    print("Filesystem...")
    from modules.filesystem import *
    print("done. Network...")
    from modules.network import *
    print("done. Settings...")
    from modules.settings import *
    print("done. Python...")
    from modules.python import *
    print("done. Audio...")
    from modules.audio import *
    print("done. Console...")
    from modules.console import *
    print("done. Process...")
    from modules.process import *
    print("done. Msgbox...")
    from modules.msgbox import *
    print("done. Web...")
    from modules.web import *
    print("done. Mod...")
    from modules.mod import *
    print("done. Control...")
    from modules.control import *
    print("done. Colorama")
    from colorama import Fore, Back
    print("done.")
    print("Loading commands")
    commands = {
        "mkdir":mkdir,
        "rmdir":rmdir,
        "list":listt,
        "write":write,
        "read":read,
        "remove":remove,
        "copy":copy,
        "rename":rename,
        "move":rename,
        "ping":ping,
        "getrt":getrt,
        "getrsc":getrsc,
        "download":download,
        "setusername":setusername,
        "setstartup":setstartup,
        "exec":execc,
        "playaudio":playaudio,
        "stopaudio":stopaudio,
        "clear":clear,
        "processes":processes,
        "kill":kill,
        "terminate":terminate,
        "suspend":suspend,
        "resume":resume,
        "processinfo":processinfo,
        "msgboxerror":msgboxerror,
        "msgboxinfo":msgboxinfo,
        "msgboxwarning":msgboxwarning,
        "start":start,
        "out":out,
        "mmove":mmove,
        "mrep":mrep,
        "mpos":mpos,
        "kpress":kpress,
        "kwrite":kwrite,
        "wait":wait,
        "openurl":openurl,
        "modinstall":modinstall,
        "moduninstall":moduninstall
    }
    print("done")
    os.system("cls")
    os.system("title TypeShell 1.3.2")
    print(r("C:/TypeShell/userdata/startup"))
    if len(sys.argv) == 1:
        cd = os.getcwd()
    else:
        cd = sys.argv[1]
    while True:
        username = r("C:/TypeShell/userdata/username")
        print(f"{Fore.GREEN}@{username} {Fore.BLUE}~{cd}{Fore.RESET} $ ", end="")
        inp = input().replace(" & ", "&").split("&")
        for line in inp:
            lin = line.split(" ")
            command = lin[0]
            args = lin
            args.remove(command)
            try:
                commands[command](args)
            except KeyError:
                try:
                    w("C:/TypeShell/modules/args.txt", " ".join(args))
                    exec(r(f"C:/TypeShell/modules/{command}.py"))
                except FileNotFoundError:
                    print("Команда не найдена")
                except Exception as err:
                    print(err)
            except Exception as err:
                print(err)
except KeyboardInterrupt:
    os.system("cls")
    pass