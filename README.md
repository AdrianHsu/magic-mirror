#Magic Mirror

arecord -r 16000 -f S6_LE tmp.wav  
wf = wave.open("tmp.wav")  
wf.getframerate() is 16000 (sample rate: 16000)  
wf.getnchannels() is 1 (channel)  
wf.getsampwidth() is 2 (byte depth)  

#generate the WAV file content  
with io.BytesIO() as wav_file:  
wav_writer = wave.open(wav_file, "wb")  
wav_writer.setframerate(16000)  
wav_data = wav_file.getvalue()  
finally... wav_writer.close()  

#Subprocess control

[http://xmodulo.com/how-to-capture-microphone-input-to-wav-format-file.html](http://xmodulo.com/how-to-capture-microphone-input-to-wav-format-file.html)  

sudo apt-get install mediainfo  
proc = subprocess.Popen(cmd, shell=True)  
in parent:  
os.system("pkill -9 arecord")  
proc.terminate()  