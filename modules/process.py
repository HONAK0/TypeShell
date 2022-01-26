import psutil

def processes(args):
    pids = psutil.pids()
    for pid in pids:
        print(f"Name:{psutil.Process(pid).name()} pid:{pid}")
def kill(args):
    pids = psutil.pids()
    found = False
    for pid in pids:
        if ".exe" in args[0]:
            if psutil.Process(pid).name() == args[0]:
                found = True
                psutil.Process(pid).kill()
        else:
            if pid == int(args[0]):
                found = True
                psutil.Process(pid).kill()
    if not found:
        print("Процесс не найден")
def terminate(args):
    pids = psutil.pids()
    found = False
    for pid in pids:
        if ".exe" in args[0]:
            if psutil.Process(pid).name() == args[0]:
                found = True
                psutil.Process(pid).terminate()
        else:
            if pid == int(args[0]):
                found = True
                psutil.Process(pid).terminate()
    if not found:
        print("Процесс не найден")
def suspend(args):
    pids = psutil.pids()
    found = False
    for pid in pids:
        if ".exe" in args[0]:
            if psutil.Process(pid).name() == args[0]:
                found = True
                psutil.Process(pid).suspend()
        else:
            if pid == int(args[0]):
                found = True
                psutil.Process(pid).suspend()
    if not found:
        print("Процесс не найден")
def resume(args):
    pids = psutil.pids()
    found = False
    for pid in pids:
        if ".exe" in args[0]:
            if psutil.Process(pid).name() == args[0]:
                found = True
                psutil.Process(pid).resume()
        else:
            if pid == int(args[0]):
                found = True
                psutil.Process(pid).resume()
    if not found:
        print("Процесс не найден")
def processinfo(args):
    pids = psutil.pids()
    found = False
    for pid in pids:
        if ".exe" in args[0]:
            if psutil.Process(pid).name() == args[0]:
                found = True
                d = psutil.Process(pid)
                print(f"Name:{d.name()} PID:{pid} Started:{d.create_time()} CPU:{d.cpu_percent()}% MEM:{d.memory_percent()}% Is runing:{d.is_running()} Username:{d.username()} Created time:{d.create_time()} Status:{d.status()}")
        else:
            if pid == int(args[0]):
                found = True
                d = psutil.Process(pid)
                print(f"Name:{d.name()} PID:{pid} Started:{d.create_time()} CPU:{d.cpu_percent()}% MEM:{d.memory_percent()}% Is runing:{d.is_running()} Username:{d.username()} Created time:{d.create_time()} Status:{d.status()}")
    if not found:
        print("Процесс не найден")