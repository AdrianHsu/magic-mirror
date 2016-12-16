import os
import subprocess
import time

#os.system("arecord -r 16000 -f S16_LE tmp.wav")
cmd = "arecord -r 16000 -f S16_LE tmp.wav"
proc = subprocess.Popen(cmd, shell=True)
time.sleep(3)
print("test")
os.system("pkill -9 arecord")
proc.terminate()
