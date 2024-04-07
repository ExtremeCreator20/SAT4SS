"""import os, socket, ctypes

sock = socket.socket()"""


#import ctypes

import subprocess

def enable_airplane_mode():
    subprocess.run("netsh interface set interface \"Wi-Fi\" admin=disabled", shell=True)

def disable_airplane_mode():
    subprocess.run("netsh interface set interface \"Wi-Fi\" admin=enabled", shell=True)

# To turn on airplane mode
enable_airplane_mode()

# To turn off airplane mode
#disable_airplane_mode()
