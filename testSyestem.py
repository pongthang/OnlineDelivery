import subprocess
import os

subprocess.run(["ls","-l"])
#subprocess.run(["python3","buttonGui.py"])
os.chdir("hi")
subprocess.run(["git","clone","https://github.com/pongthang/pongthang.github.io.git"])
#subprocess.run(["python3","oop.py"])