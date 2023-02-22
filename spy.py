import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("VIP").Spy()
except Exception as e:
    exit(str(e))
