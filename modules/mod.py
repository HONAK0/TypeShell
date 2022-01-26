import requests
import wget
import os

servers = [
    ("https://honak0.github.io/","https://honak0.github.io/typeshell/mods/")
]
def res(args):
    modinstall(args)
def modinstall(args):
    if len(args) == 0:
        print("Введите аргументы")
        return
    founds = []
    for server in servers:
        try:
            print(f"{server[0]} - ", end="")
            d = requests.get(server[0])
            print(f"{d.status_code} - ",end="")
            if d.status_code == 200:
                print("ok")
                founds.append(server)
            else:
                print("error")
        except:
            res(args)
    if len(founds) == 0:
        print("К сожелению все сервера отключены либо удалены")
        return
    print(f"Подготовка к загрузке с сервера '{founds[0][0]}'")
    try:
        wget.download(f"{founds[0][1]}{args[0]}.py", "C:/TypeShell/modules/")
        print()
        print("Команда успешно установленна!")
    except:
        print("Команда не найдена на сервере")
def moduninstall(args):
    if len(args) == 0:
        print("Введите аргументы")
        return
    if os.path.exists(f"C:/TypeShell/modules/{args[0]}.py"):
        print("Удаляю...")
        os.remove(f"C:/TypeShell/modules/{args[0]}.py")
        print("Готово")
    else:
        print("Команды не существует")