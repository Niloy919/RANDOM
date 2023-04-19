import os, sys
os.system('git pull')
try:
    __import__("RANDOM").main()
except Exception as e:
    exit(str(e))
