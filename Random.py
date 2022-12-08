import os, sys
try:
    __import__("Johnny").main()
except Exception as e:
    exit(str(e))
