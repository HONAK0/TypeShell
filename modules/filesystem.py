import os
import shutil

def mkdir(args):
    if os.path.exists(args[0]):
        print("Папка уже существует")
    else:
        os.mkdir(args[0])
        print("Готово")
def rmdir(args):
    if not os.path.exists(args[0]):
        print("Папка не существует")
    else:
        shutil.rmtree(args[0])
        print("Готово")
def listt(args):
    if len(args) == 1:
        if os.path.exists(args[0]):
            print("\n".join(os.listdir(args[0])))
        else:
            print("Папки не существует")
    else:
        print("\n".join(os.listdir()))
def write(args):
    filename = args[0]
    value = args
    value.remove(value[0])
    open(filename, "w", encoding="utf8").write(" ".join(value))
def read(args):
    if not os.path.exists(args[0]):
        print("Файла не существует")
    else:
        print(open(args[0], "r", encoding="utf8").read())
def remove(args):
    if not os.path.exists(args[0]):
        print("Файла не существует")
    else:
        os.remove(args[0])
def copy(args):
    if not os.path.exists(args[0]):
        print("Файла не существует")
    else:
        if os.path.exists(args[1]):
            print("Файла существует")
        else:
            shutil.copy(args[0],args[1])
def rename(args):
    if not os.path.exists(args[0]):
        print("Файл или папка не существует")
    else:
        if os.path.exists(args[1]):
            print("Файл или папка существует")
        else:
            os.rename(args[0],args[1])
def start(args):
    if not os.path.exists(args[0]):
        print("Файл или папка не существует")
    else:
        os.startfile(args[0])