import os, sys
try:
    __import__("AK4").main()
except Exception as e:
    exit(str(e))
