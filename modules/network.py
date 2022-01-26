import requests
import wget
import time

def ping(args):
    start = time.time()
    requests.get(args[0])
    end = time.time()
    res = "{0:.2f}".format(end - start)
    print(f"Время ответа: {res} секунд")
def getrt(args):
    tex = requests.get(args[0]).text
    print(tex)
def getrsc(args):
    code = requests.get(args[0]).status_code
    print(code)
def download(args):
    wget.download(args[0], args[1])
    print()